import unittest
import os
import sys
import json
from unittest.mock import patch, MagicMock

# Ensure project root is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Gemini_Modules.gemini_ffmpeg_synthesis import (
    GeminiFFmpegEngine,
    FFmpegCommandGenerator,
    RefinementLoop
)

class TestGeminiFFmpegSynthesis(unittest.TestCase):

    def setUp(self):
        self.engine = GeminiFFmpegEngine()
        self.cmd_gen = FFmpegCommandGenerator()

    def test_watermark_overlay_dispatch(self):
        """Verify watermark_overlay op dispatch generates valid command steps."""
        dummy_wm = os.path.abspath("dummy_wm.png")
        with open(dummy_wm, "w") as f:
            f.write("dummy")

        try:
            plan = {
                "editing_intent": "Test Watermark Overlay",
                "operations": [
                    {
                        "operation_type": "watermark_overlay",
                        "watermark_path": dummy_wm,
                        "position": "top_right",
                        "scale": 0.2,
                        "opacity": 0.85
                    }
                ]
            }
            res = self.engine.synthesize_from_gemini_json(plan, "input.mp4", "output.mp4")
            self.assertEqual(res["total_steps"], 1)
            step = res["command_steps"][0]
            self.assertEqual(step["operation"], "watermark_overlay")
            self.assertIn("-filter_complex", step["cmd_list"])
            self.assertIn(dummy_wm, step["cmd_list"])
        finally:
            if os.path.exists(dummy_wm):
                os.remove(dummy_wm)

    def test_global_encoding_customization(self):
        """Verify custom global_encoding (codec, preset, crf) overrides defaults."""
        plan = {
            "editing_intent": "Test Global Encoding",
            "global_encoding": {
                "codec": "libx265",
                "preset": "slow",
                "crf": 22
            },
            "operations": [
                {"operation_type": "scale_aspect", "mode": "crop"}
            ]
        }
        res = self.engine.synthesize_from_gemini_json(plan, "input.mp4", "output.mp4")
        step = res["command_steps"][0]
        cmd_str = step["terminal_command"]
        self.assertIn("libx265", cmd_str)
        self.assertIn("slow", cmd_str)
        self.assertIn("22", cmd_str)

    def test_score_execution_breakdown(self):
        """Verify score_execution returns itemized breakdown and failed_criteria."""
        refinement = RefinementLoop(self.engine)
        context = {
            "problem_areas": ["Watermark logo in top right"],
            "recommended_aspect": "9:16",
            "audio_inference": "voiceover speech"
        }
        synthesis_res = {
            "command_steps": [
                {"operation": "scale_aspect"}
            ]
        }
        res = refinement.score_execution(context, synthesis_res)
        self.assertIsInstance(res, dict)
        self.assertIn("score", res)
        self.assertIn("breakdown", res)
        self.assertIn("failed_criteria", res)
        self.assertIn("passed_criteria", res)
        self.assertLess(res["score"], 0.75)
        self.assertTrue(any("Watermark" in item for item in res["failed_criteria"]))
        self.assertTrue(any("Voiceover" in item for item in res["failed_criteria"]))

    def test_offline_fallback_watermark_injection(self):
        """Verify offline fallback auto-injects delogo_blur when forensic_context contains a watermark."""
        forensic_context = {
            "watermark_detected": True,
            "items": [{"x": 50, "y": 20, "w": 120, "h": 40}]
        }
        res = self.engine.run_full_pipeline(
            user_request="Offline test",
            input_video_path="input.mp4",
            output_video_path="output.mp4",
            forensic_context=forensic_context,
            dry_run=True
        )
        self.assertIsNotNone(res)
        steps = res["executed_steps"]
        op_types = [s["operation"] for s in steps]
        self.assertIn("delogo_blur", op_types)
        self.assertIn("scale_aspect", op_types)

    def test_precision_speed_snapping(self):
        """Verify compute_precision_speed_factor snaps to nearest audio beat timestamp."""
        # Source video 10.0s long, raw speed 1.25x -> target 8.0s. Nearest beat is 7.5s -> factor = 10.0/7.5 = 1.3333
        audio_beats = [2.0, 4.0, 6.0, 7.5, 9.0]
        speed_factor = self.cmd_gen.compute_precision_speed_factor(
            source_duration_s=10.0,
            target_duration_s=8.0,
            audio_beats_s=audio_beats
        )
        self.assertEqual(speed_factor, 1.3333)

    def test_run_full_pipeline_end_to_end_dry_run(self):
        """Verify run_full_pipeline completes end-to-end in dry_run mode without NameError or Name/Wiring exceptions."""
        forensic_context = {
            "watermark_detected": True,
            "items": [{"x": 15, "y": 15, "w": 150, "h": 50}],
            "watermark_path": os.path.abspath("dummy_wm.png")
        }
        res = self.engine.run_full_pipeline(
            user_request="Full end-to-end integration test",
            input_video_path="input.mp4",
            output_video_path="output.mp4",
            forensic_context=forensic_context,
            dry_run=True
        )
        self.assertEqual(res["status"], "SUCCESS")
        self.assertEqual(res["mode"], "DRY_RUN")
        self.assertGreaterEqual(res["total_steps"], 2)

    def test_top_level_concat_op_dispatch(self):
        """Verify top-level concat op in Gemini plan dispatches build_concat_command."""
        plan = {
            "editing_intent": "Test Concat Dispatch",
            "operations": [
                {
                    "operation_type": "concat",
                    "inputs": ["input.mp4"]
                }
            ]
        }
        res = self.engine.synthesize_from_gemini_json(plan, "input.mp4", "output.mp4")
        self.assertEqual(res["total_steps"], 1)
        step = res["command_steps"][0]
        self.assertEqual(step["operation"], "concat")

    def test_delogo_band_parameter_preservation(self):
        """Verify build_delogo_blur_command includes :band= inside filter string and is preserved in cmd_list."""
        cmd = self.cmd_gen.build_delogo_blur_command("input.mp4", "output.mp4", x=10, y=20, w=100, h=50, band=4)
        filter_arg = next(arg for i, arg in enumerate(cmd["cmd_list"]) if cmd["cmd_list"][i-1] == "-vf")
        self.assertIn(":band=4", filter_arg)

        # Test synthesize_from_gemini_json generates and preserves :band=4
        plan = {
            "editing_intent": "Test Band Preservation",
            "operations": [{"operation_type": "delogo_blur", "x": 10, "y": 20, "w": 100, "h": 50, "band": 4}]
        }
        synth = self.engine.synthesize_from_gemini_json(plan, "input.mp4", "output.mp4")
        step_vf = next(arg for i, arg in enumerate(synth["command_steps"][0]["cmd_list"]) if synth["command_steps"][0]["cmd_list"][i-1] == "-vf")
        self.assertIn(":band=4", step_vf)

    @patch("subprocess.run")
    def test_execute_pipeline_preserves_band_parameter_mocked(self, mock_run):
        """Verify execute_pipeline in non-dry_run mode passes :band=4 in subprocess.run clean_cmd."""
        mock_run.return_value = MagicMock(returncode=0, stdout="", stderr="")
        plan = {
            "editing_intent": "Mocked Exec Band Check",
            "operations": [{"operation_type": "delogo_blur", "x": 10, "y": 20, "w": 100, "h": 50, "band": 4}]
        }
        res = self.engine.execute_pipeline(plan, "input.mp4", "output.mp4", dry_run=False)
        self.assertEqual(res["status"], "SUCCESS")
        
        # Verify subprocess.run was called with clean_cmd containing :band=4
        called_cmd = mock_run.call_args[0][0]
        filter_arg = next(arg for i, arg in enumerate(called_cmd) if called_cmd[i-1] == "-vf")
        self.assertIn(":band=4", filter_arg)

    def test_run_id_concurrency_isolation(self):
        """Verify consecutive synthesis runs generate distinct run_id temp file paths."""
        plan = {
            "editing_intent": "Multi Step Test",
            "operations": [
                {"operation_type": "delogo_blur", "x": 0, "y": 0, "w": 10, "h": 10},
                {"operation_type": "scale_aspect", "target_width": 1080, "target_height": 1920}
            ]
        }
        s1 = self.engine.synthesize_from_gemini_json(plan, "input.mp4", "output.mp4")
        s2 = self.engine.synthesize_from_gemini_json(plan, "input.mp4", "output.mp4")
        out1 = s1["command_steps"][0]["output"]
        out2 = s2["command_steps"][0]["output"]
        self.assertNotEqual(out1, out2)

if __name__ == "__main__":
    unittest.main()

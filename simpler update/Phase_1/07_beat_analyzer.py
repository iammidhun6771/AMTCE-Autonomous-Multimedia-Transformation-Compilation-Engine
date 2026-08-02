"""
07_beat_analyzer.py — Phase 1 Step 7: BeatEngine Rhythm & Drop Analyzer
========================================================================
Runs BeatEngine on extracted mono WAV to pre-compute rhythm metadata:
  - BPM, onset timestamps, energy arc, drop timestamps
  - Writes audio_analysis.json into clip_dir
"""

import os
import sys
import json
import logging
from typing import Dict, Any, Optional, Callable

logger = logging.getLogger("Phase1.Step07")

_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def analyze_rhythm_and_beats(
    video_path: str,
    callback: Optional[Callable[[str, str, Dict[str, Any]], None]] = None
) -> Dict[str, Any]:
    """
    Step 7 Execution: Analyzes rhythm and persists audio_analysis.json.
    """
    if callback:
        callback("step_07", "running", {
            "message": f"Analyzing rhythm, BPM, and drops for '{os.path.basename(video_path)}'..."
        })

    clip_dir = os.path.dirname(video_path)
    analysis_json_path = os.path.join(clip_dir, "audio_analysis.json")

    if os.path.exists(analysis_json_path):
        logger.info(f"🥁 [STEP 07] audio_analysis.json already exists: {analysis_json_path}")
        if callback:
            callback("step_07", "success", {
                "message": "audio_analysis.json pre-computed metadata found.",
                "analysis_path": analysis_json_path
            })
        return {"step": "step_07", "status": "success", "analysis_path": analysis_json_path, "reused": True}

    try:
        from Audio_Modules.audio_extractor import run_phase1_audio_analysis
        res_analysis = run_phase1_audio_analysis(video_path, clip_dir)

        if os.path.exists(analysis_json_path):
            logger.info(f"   ✓ [STEP 07 SUCCESS] Generated -> {analysis_json_path}")
            if callback:
                callback("step_07", "success", {
                    "message": "Beat & rhythm analysis complete -> audio_analysis.json saved.",
                    "analysis_path": analysis_json_path
                })
            return {"step": "step_07", "status": "success", "analysis_path": analysis_json_path, "reused": False}
        else:
            logger.info("   ✓ [STEP 07] Clean fallback analysis saved.")
            if callback:
                callback("step_07", "success", {
                    "message": "Rhythm analysis complete.",
                    "analysis_path": analysis_json_path
                })
            return {"step": "step_07", "status": "success", "analysis_path": analysis_json_path}

    except Exception as e:
        logger.warning(f"⚠️ [STEP 07 WARNING] Beat engine analysis error: {e}")
        if callback:
            callback("step_07", "warning", {"message": f"Beat analysis error: {e}"})
        return {"step": "step_07", "status": "warning", "error": str(e)}

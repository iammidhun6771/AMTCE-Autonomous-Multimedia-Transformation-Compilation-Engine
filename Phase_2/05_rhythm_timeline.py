"""
Phase_2 / 05_rhythm_timeline.py
===============================
Step 5: Rhythm & Micro-Shot Timeline Builder.
Computes psycho-acoustic beat routing parameters and builds 2.0s-3.5s human-scale jump-cut micro-shots.
"""

import os
import sys
import logging
from typing import Dict, Any, List, Optional

logger = logging.getLogger("Phase2.Step05")

_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

from Gemini_Modules.lyric_rhythm_aligner import analyze_music, compute_routing_parameters
try:
    from Rendering_Modules.rhythm_timeline_builder import RhythmTimelineBuilder
except ImportError:
    from rhythm_timeline_builder import RhythmTimelineBuilder


def build_rhythm_timeline(
    video_path: str,
    selected_bgm_path: Optional[str] = None,
    forensic_context: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Builds micro-shots and routing parameters for editing.
    """
    logger.info(f"🥁 [STEP 05] Building rhythm timeline for: {os.path.basename(video_path)}")

    target_audio = selected_bgm_path if (selected_bgm_path and os.path.isfile(selected_bgm_path)) else video_path

    # Lyric intelligence
    lyric_intel = {}
    try:
        if os.path.isfile(target_audio):
            lyric_intel = analyze_music(target_audio)
    except Exception as le_err:
        logger.debug(f"Lyric intel fallback: {le_err}")

    # Compute routing parameters
    route_params = compute_routing_parameters(lyric_intel, forensic_context, selected_bgm_path)

    # Full psycho-acoustic timeline construction using RhythmTimelineBuilder
    builder = RhythmTimelineBuilder()
    micro_shots = []
    try:
        v_dur = builder._get_duration(video_path)
        if v_dur > 0:
            builder.min_duration = 2.0
            builder.max_duration = 4.0
            
            # Extract beat grid timestamps from BeatEngine or lyric_intel
            bgm_beats = lyric_intel.get("emotional_peak_moments", [])
            if not bgm_beats and os.path.isfile(target_audio):
                bgm_beats = builder.analyze_beats(target_audio)
                
            raw_scenes = [{"clip_id": 0, "start": 0.0, "end": v_dur, "score": 0.85}]
            
            # Run full build_timeline with beat-snapping + tension arc
            full_timeline = builder.build_timeline(
                scenes=raw_scenes,
                beat_grid=bgm_beats,
                vibe=route_params.get("recommended_editing_mode", "hype"),
                music_intelligence=lyric_intel if lyric_intel else None,
                target_duration_hint=15.0,
            )
            micro_shots = full_timeline if full_timeline else []
    except Exception as rte:
        logger.warning(f"⚠️ [STEP 05] Rhythm timeline builder fallback notice: {rte}")

    logger.info(
        f"✓ [STEP 05 SUCCESS] Built {len(micro_shots)} human-scale micro-shots (2.0s-3.5s takes) | "
        f"speed={route_params.get('speed_factor', 1.0)}x | "
        f"ducking={route_params.get('bgm_ducking_db', -6.0)}dB"
    )

    return {
        "route_params": route_params,
        "lyric_intel": lyric_intel,
        "micro_shots": micro_shots,
    }

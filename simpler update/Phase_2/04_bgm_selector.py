"""
Phase_2 / 04_bgm_selector.py
============================
Step 4: Gemini Call 2 — BGM Selector.
Cross-matches clip's visual_context + audio_data vs ALL pooled clip audio records from ClipIntelligenceStore.
Selects single best BGM track and saves decision to clip intelligence JSON.
"""

import os
import sys
import logging
from typing import Dict, Any, Optional

logger = logging.getLogger("Phase2.Step04")

_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

from Gemini_Modules.lyric_rhythm_aligner import select_best_audio_for_clip
from Audio_Modules.audio_pool_manager import AudioPoolManager


def select_clip_bgm(
    clip_id: str,
    clip_folder: Optional[str] = None,
    audio_dir: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Executes Gemini Call 2 BGM Selector.
    Returns dict containing selected_audio_track, full physical path, and alignment score.
    """
    logger.info(f"🎶 [STEP 04] Running Gemini Call 2 BGM Selector for clip '{clip_id}'...")

    res = select_best_audio_for_clip(clip_id=clip_id, clip_folder=clip_folder, audio_dir=audio_dir)
    selected_track_name = res.get("selected_audio_track")

    # Resolve physical path
    resolved_path = None
    if audio_dir is None:
        audio_dir = os.path.join(_REPO_ROOT, "Original_audio")

    if selected_track_name:
        for candidate_dir in [
            os.path.join(audio_dir, "active"),
            audio_dir,
            os.path.join(audio_dir, "cooldown"),
        ]:
            if os.path.isdir(candidate_dir):
                candidate_path = os.path.join(candidate_dir, selected_track_name)
                if os.path.isfile(candidate_path):
                    resolved_path = candidate_path
                    break

    # Fallback to pool manager if not found
    if not resolved_path:
        try:
            pool = AudioPoolManager(base_dir=audio_dir)
            resolved_path = pool.select_best_audio()
            if resolved_path:
                selected_track_name = os.path.basename(resolved_path)
        except Exception as pool_err:
            logger.warning(f"⚠️ [STEP 04] BGM pool manager fallback notice: {pool_err}")

    res["physical_path"] = resolved_path
    logger.info(
        f"✓ [STEP 04 SUCCESS] BGM Selected: '{selected_track_name}' "
        f"(score={res.get('alignment_score', 0.0):.2f}) -> {resolved_path}"
    )
    return res

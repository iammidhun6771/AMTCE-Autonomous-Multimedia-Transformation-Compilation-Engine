"""
06_audio_extractor.py — Phase 1 Step 6: Mono 16kHz Audio Extractor
====================================================================
Extracts clean mono 16kHz PCM WAV audio from video.mp4:
  video.mp4 -> {stem}_extracted.wav
Saves the extracted ambient audio directly in the clip folder.
"""

import os
import sys
import logging
from typing import Dict, Any, Optional, Callable

logger = logging.getLogger("Phase1.Step06")

_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def extract_clip_audio(
    video_path: str,
    callback: Optional[Callable[[str, str, Dict[str, Any]], None]] = None
) -> Dict[str, Any]:
    """
    Step 6 Execution: Extracts mono 16kHz WAV audio.
    """
    if callback:
        callback("step_06", "running", {
            "message": f"Extracting mono 16kHz audio from '{os.path.basename(video_path)}'..."
        })

    clip_dir = os.path.dirname(video_path)
    stem = os.path.splitext(os.path.basename(video_path))[0]
    wav_path = os.path.join(clip_dir, f"{stem}_extracted.wav")

    if os.path.exists(wav_path):
        logger.info(f"🎵 [STEP 06] Extracted audio WAV already exists: {wav_path}")
        if callback:
            callback("step_06", "success", {
                "message": "Extracted audio WAV file already exists.",
                "wav_path": wav_path
            })
        return {"step": "step_06", "status": "success", "wav_path": wav_path, "reused": True}

    try:
        from Audio_Modules.audio_extractor import extract_audio
        success = extract_audio(video_path, wav_path)

        if success and os.path.exists(wav_path):
            logger.info(f"   ✓ [STEP 06 SUCCESS] Extracted WAV -> {wav_path}")
            if callback:
                callback("step_06", "success", {
                    "message": f"Extracted audio WAV: {os.path.basename(wav_path)}",
                    "wav_path": wav_path
                })
            return {"step": "step_06", "status": "success", "wav_path": wav_path, "reused": False}
        else:
            logger.warning(f"⚠️ [STEP 06] Video has no audio stream or extraction produced no WAV.")
            if callback:
                callback("step_06", "success", {
                    "message": "Video has no audio stream. Skipping WAV extraction.",
                    "wav_path": None
                })
            return {"step": "step_06", "status": "success", "wav_path": None, "has_audio": False}

    except Exception as e:
        logger.warning(f"⚠️ [STEP 06 WARNING] Audio extraction error: {e}")
        if callback:
            callback("step_06", "warning", {"message": f"Audio extraction error: {e}"})
        return {"step": "step_06", "status": "warning", "error": str(e)}

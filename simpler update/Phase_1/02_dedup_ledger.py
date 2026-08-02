"""
02_dedup_ledger.py — Phase 1 Step 2: Content Deduplication & Disk Checker
===========================================================================
Checks if a reel shortcode or URL has already been processed or downloaded
using:
  - Content_Scraper_Modules/content_ledger.py
  - Local disk existence check in downloads/{owner}_{shortcode}/
"""

import os
import sys
import logging
from typing import Dict, Any, Optional, Callable

logger = logging.getLogger("Phase1.Step02")

_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def check_deduplication(
    shortcode: str,
    owner: str = "actress",
    downloads_dir: Optional[str] = None,
    callback: Optional[Callable[[str, str, Dict[str, Any]], None]] = None
) -> Dict[str, Any]:
    """
    Step 2 Execution: Verifies if clip shortcode is clean/unique or already on disk.
    """
    if callback:
        callback("step_02", "running", {"message": f"Checking deduplication for shortcode '{shortcode}'..."})

    if not downloads_dir:
        downloads_dir = os.path.join(_REPO_ROOT, "downloads")

    clip_folder_name = f"{owner}_{shortcode}"
    clip_dir = os.path.join(downloads_dir, clip_folder_name)

    meta_path = os.path.join(clip_dir, "metadata.json")
    video_path = os.path.join(clip_dir, "video.mp4")

    # 1. Disk presence check
    already_on_disk = os.path.exists(meta_path) and os.path.exists(video_path)

    # 2. Content Ledger check
    ledger_processed = False
    try:
        from Content_Scraper_Modules.content_ledger import get_ledger
        ledger = get_ledger()
        if hasattr(ledger, "is_downloaded") and callable(ledger.is_downloaded):
            ledger_processed = ledger.is_downloaded(shortcode)
    except Exception as e:
        logger.debug(f"Ledger check warning: {e}")

    is_duplicate = already_on_disk or ledger_processed

    res = {
        "step": "step_02",
        "shortcode": shortcode,
        "is_duplicate": is_duplicate,
        "already_on_disk": already_on_disk,
        "clip_dir": clip_dir,
        "video_path": video_path if already_on_disk else None
    }

    if is_duplicate:
        logger.info(f"♻️ [STEP 02] Shortcode '{shortcode}' already downloaded. Skipping scraper.")
        if callback:
            callback("step_02", "success", {
                "message": f"Clip '{shortcode}' exists on disk in downloads/. Skipping fetch.",
                "is_duplicate": True,
                "clip_dir": clip_dir
            })
    else:
        logger.info(f"✨ [STEP 02] Shortcode '{shortcode}' is NEW & clean to download.")
        if callback:
            callback("step_02", "success", {
                "message": f"Clip '{shortcode}' verified unique and ready for download.",
                "is_duplicate": False,
                "clip_dir": clip_dir
            })

    return res

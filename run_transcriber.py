"""
run_transcriber.py — AMTCE Root Transcriber Entrypoint
======================================================
Root standalone wrapper for Clip_Transcriber_Module.

Usage:
  python run_transcriber.py --video <path_to_clip.mp4>
  python run_transcriber.py --folder <path_to_clips_dir>
"""

import os
import sys
import runpy

_REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
_MODULE_PATH = os.path.join(_REPO_ROOT, "Clip_Transcriber_Module")

if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
if _MODULE_PATH not in sys.path:
    sys.path.insert(0, _MODULE_PATH)

if __name__ == "__main__":
    target_script = os.path.join(_MODULE_PATH, "standalone_run.py")
    runpy.run_path(target_script, run_name="__main__")

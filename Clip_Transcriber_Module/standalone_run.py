"""
Clip_Transcriber_Module / standalone_run.py
============================================
Standalone CLI execution script for Clip_Transcriber_Module.

Usage:
  python standalone_run.py --video <path_to_video.mp4>
  python standalone_run.py --folder <path_to_folder_with_videos>
"""

import os
import sys
import argparse
import json
import logging

# Ensure UTF-8 output encoding for Windows consoles
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

_MODULE_DIR = os.path.dirname(os.path.abspath(__file__))
_REPO_ROOT = os.path.dirname(_MODULE_DIR)

if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
if _MODULE_DIR not in sys.path:
    sys.path.insert(0, _MODULE_DIR)

from clip_transcriber import ClipTranscriber

logger = logging.getLogger("ClipTranscriberCLI")


def main():
    parser = argparse.ArgumentParser(description="AMTCE Standalone Clip Transcriber & Gemini Semantic Enhancer")
    parser.add_argument("--video", type=str, help="Path to a single video clip file (.mp4, .mov, etc.)")
    parser.add_argument("--folder", type=str, help="Path to a directory containing video clip files")
    parser.add_argument("--model", type=str, default="base", help="Faster-Whisper model size (tiny, base, small, medium, large-v3)")
    parser.add_argument("--output", type=str, default=None, help="Custom output directory")

    args = parser.parse_args()

    if not args.video and not args.folder:
        print("\n[ERROR] Please provide either --video or --folder argument.")
        parser.print_help()
        sys.exit(1)

    transcriber = ClipTranscriber(whisper_model_size=args.model)

    if args.video:
        video_path = os.path.abspath(args.video)
        if not os.path.exists(video_path):
            print(f"[ERROR] Video file not found: {video_path}")
            sys.exit(1)

        result = transcriber.process_clip(video_path, output_dir=args.output)
        print("\n" + "=" * 60)
        print("TRANSCRIBER PIPELINE COMPLETED SUCCESSFULLY!")
        print("=" * 60)
        print(f"Accurate Transcript: {result.get('accurate_full_transcript')}")
        print(f"Topic: {result.get('semantic_context', {}).get('topic')}")
        print(f"Corrections Made: {len(result.get('whisper_corrections', []))}")
        print("=" * 60)

    elif args.folder:
        folder_path = os.path.abspath(args.folder)
        if not os.path.exists(folder_path):
            print(f"[ERROR] Folder not found: {folder_path}")
            sys.exit(1)

        valid_exts = (".mp4", ".mov", ".mkv", ".avi", ".webm")
        files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.lower().endswith(valid_exts)]

        if not files:
            print(f"[WARNING] No video files found in folder: {folder_path}")
            sys.exit(0)

        print(f"Found {len(files)} video clips in {folder_path}. Processing...")
        for i, vid in enumerate(files, 1):
            print(f"\n[{i}/{len(files)}] Processing: {os.path.basename(vid)}")
            try:
                transcriber.process_clip(vid, output_dir=args.output)
            except Exception as e:
                print(f"[ERROR] Failed processing {os.path.basename(vid)}: {e}")

        print("\nBatch transcription processing completed.")


if __name__ == "__main__":
    main()

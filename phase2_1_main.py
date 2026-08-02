"""
phase2_1_main.py — Phase 2.1 Watermark Cleanup Gate
===================================================
Standalone interception stage placed between Phase 2 render completion
and Telegram chat delivery.

Usage:
    python phase2_1_main.py "D:\\path\\to\\rendered_master.mp4"
"""

import argparse
import logging
import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)

logger = logging.getLogger("phase2_1_main")
logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(name)s | %(message)s")


def run_phase2_1_watermark_gate(input_path: str, output_path: str = None, keywords: str = "", retry_level: int = 0):
    """Run the watermark cleanup stage and return the final cleaned video path."""
    from Watermark_and_Inpainting.watermark_main import run_watermark_removal

    cleaned_path, status_log = run_watermark_removal(
        input_path=input_path,
        output_path=output_path,
        keywords=keywords,
        retry_level=retry_level,
    )

    logger.info("[PHASE 2.1] Watermark cleanup completed: %s", cleaned_path)
    return cleaned_path, status_log


def main():
    parser = argparse.ArgumentParser(description="AMTCE Phase 2.1 Watermark Cleanup Gate")
    parser.add_argument("input", help="Path to rendered master reel to clean before Telegram delivery")
    parser.add_argument("-o", "--output", help="Optional cleaned output path")
    parser.add_argument("-k", "--keywords", default="", help="Optional watermark detection hints")
    parser.add_argument("--retry", type=int, default=0, help="Retry level (0-2)")
    args = parser.parse_args()

    input_path = os.path.abspath(args.input)
    if not os.path.exists(input_path):
        logger.error("Input video not found: %s", input_path)
        sys.exit(1)

    cleaned_path, status_log = run_phase2_1_watermark_gate(
        input_path=input_path,
        output_path=args.output,
        keywords=args.keywords,
        retry_level=args.retry,
    )

    print(f"\n✅ [PHASE 2.1 COMPLETE] Cleaned path: {cleaned_path}")
    print(status_log)


if __name__ == "__main__":
    main()

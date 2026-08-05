"""
Clip_Transcriber_Module
========================
AMTCE Standalone Audio Extraction, Faster-Whisper Transcription,
and Gemini Multimodal Cross-Referencing Context Engine.
"""

from .clip_transcriber import ClipTranscriber, transcribe_and_enhance_clip

__all__ = ["ClipTranscriber", "transcribe_and_enhance_clip"]

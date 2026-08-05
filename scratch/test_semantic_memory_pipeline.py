import os
import sys
import json

# Add Audio_Modules and Gemini_Modules to sys.path
repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
audio_modules_path = os.path.join(repo_root, "Audio_Modules")
gemini_modules_path = os.path.join(repo_root, "Gemini_Modules")
sys.path.insert(0, repo_root)
sys.path.insert(0, audio_modules_path)
sys.path.insert(0, gemini_modules_path)

def test_persistent_lyric_cache():
    print("--- 1. Testing Persistent Lyric Cache ---")
    from lyric_rhythm_aligner import analyze_music, _empty_report

    # Test file path
    beats_dir = os.path.join(repo_root, "Original_audio", "beats")
    os.makedirs(beats_dir, exist_ok=True)
    test_cache_path = os.path.join(beats_dir, "test_audio_sample_lyric.json")

    # Create dummy persistent cache file
    dummy_data = {
        "has_vocals": True,
        "language": "English",
        "tempo_bpm": 120.0,
        "bar_duration_sec": 2.0,
        "dominant_emotion": "intimate",
        "energy_profile": "medium",
        "sections": [{"start": 0.0, "end": 10.0, "type": "verse", "energy": 0.5}],
        "lyrics": [{"time": 1.0, "end": 3.0, "text": "baby come closer", "emotion_weight": 0.9, "emotion_tag": "intimate"}],
        "vibe_tags": ["aesthetic", "photoshoot", "intimate"],
        "_source": "gemini"
    }

    with open(test_cache_path, "w", encoding="utf-8") as f:
        json.dump(dummy_data, f, indent=2)
    print(f"Created test cache file: {test_cache_path}")

    # Call analyze_music on dummy path to verify cache hit
    dummy_audio_path = os.path.join(beats_dir, "test_audio_sample.mp3")
    with open(dummy_audio_path, "wb") as f:
        f.write(b"\x00" * 40000) # > 32KB

    report = analyze_music(dummy_audio_path)
    print(f"Report _source: {report.get('_source')}")
    print(f"Dominant emotion: {report.get('dominant_emotion')}")

    assert report.get("_source") == "cache_hit", "Expected cache_hit source!"
    assert report.get("dominant_emotion") == "intimate", "Expected dominant emotion 'intimate'!"
    print("[SUCCESS] Persistent Lyric Cache Test Passed!\n")

    # Clean up test files
    try:
        os.remove(test_cache_path)
        os.remove(dummy_audio_path)
    except:
        pass

def test_pool_manager_lyric_scoring():
    print("--- 2. Testing AudioPoolManager Lyric Scoring ---")
    from audio_pool_manager import AudioPoolManager

    pool = AudioPoolManager()
    # Test scoring logic directly
    best = pool.select_best_audio(target_bpm=120, target_energy=0.5, content_category="intimate")
    print(f"Pool best selection for 'intimate': {best}")
    print("[SUCCESS] AudioPoolManager Lyric Scoring Test Passed!\n")

def test_gemini_ffmpeg_prompt_payload():
    print("--- 3. Testing GeminiFFmpegEngine Prompt Payload Injection ---")
    from gemini_ffmpeg_synthesis import GeminiFFmpegEngine

    engine = GeminiFFmpegEngine()
    dummy_lyric_intel = {
        "dominant_emotion": "intimate",
        "language": "Hindi",
        "has_vocals": True,
        "vibe_tags": ["aesthetic", "slowmo"],
        "lyrics": [{"time": 2.0, "text": "teree baahon mein"}],
        "_source": "gemini"
    }

    forensic_context = {
        "subject": "Avneet Kaur",
        "style": "aesthetic photoshoot",
        "flags": ["back tattoo", "intimate lighting"]
    }

    payload = engine.generate_prompt_payload(
        user_request="Create viral 9:16 aesthetic reel with synced beat cuts.",
        forensic_context=forensic_context,
        lyric_intel=dummy_lyric_intel
    )

    user_prompt = payload.get("user_prompt", "")
    print(f"Generated user prompt snippet:\n{user_prompt[:400]}...")

    assert "Audio Lyric & Rhythm Context (Hivemind Sync)" in user_prompt, "Expected Audio Lyric context in prompt!"
    assert "teree baahon mein" in user_prompt, "Expected lyrics sample in prompt!"
    print("[SUCCESS] GeminiFFmpegEngine Prompt Payload Injection Test Passed!\n")

if __name__ == "__main__":
    test_persistent_lyric_cache()
    test_pool_manager_lyric_scoring()
    test_gemini_ffmpeg_prompt_payload()
    print("ALL TESTS PASSED SUCCESSFULLY!")

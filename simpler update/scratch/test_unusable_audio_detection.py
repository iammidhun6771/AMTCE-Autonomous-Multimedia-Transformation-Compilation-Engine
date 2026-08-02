import os
import sys
import json
import shutil

repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, repo_root)
sys.path.insert(0, os.path.join(repo_root, "Audio_Modules"))

def test_unusable_detection():
    print("--- 1. Testing Unusable Audio Fields in Lyric Aligner ---")
    from lyric_rhythm_aligner import _empty_report, _validate_and_enrich

    empty = _empty_report()
    assert "is_unusable" in empty, "Expected is_unusable key in _empty_report()"
    assert "unusable_reason" in empty, "Expected unusable_reason key in _empty_report()"

    test_dict = {
        "is_unusable": True,
        "unusable_reason": "Paparazzi shouting and street traffic with no music backing",
        "tempo_bpm": 0.0,
        "dominant_emotion": "neutral"
    }

    enriched = _validate_and_enrich(test_dict)
    assert enriched["is_unusable"] is True, "Expected is_unusable True"
    assert "Paparazzi shouting" in enriched["unusable_reason"], "Expected reason string"
    print("[SUCCESS] Lyric Aligner Unusable Fields Verified!\n")

def test_pool_quarantine_and_exclusion():
    print("--- 2. Testing Pool Quarantine & Selection Exclusion ---")
    from audio_pool_manager import AudioPoolManager

    pool = AudioPoolManager()

    # Create dummy unusable metadata entry
    unusable_file = "test_paparazzi_noise.mp3"
    pool._set_file_metadata(unusable_file, {
        "usage_count": 0,
        "last_used": 0,
        "bpm": 120.0,
        "energy": 0.8,
        "is_unusable": True,
        "unusable_reason": "Crowd shouting and stock trading hall noise"
    })
    pool._save_metadata()

    # Create dummy file in active_dir
    active_path = os.path.join(pool.active_dir, unusable_file)
    with open(active_path, "wb") as f:
        f.write(b"\x00" * 1000)

    # Verify select_best_audio excludes this file
    exclude_set = set()
    best = pool.select_best_audio(target_bpm=120, target_energy=0.8, content_category="fashion")
    assert best != unusable_file, f"Expected {unusable_file} to be excluded, but got {best}!"

    print(f"[SUCCESS] select_best_audio successfully excluded unusable file (Selected alternative: {best})\n")

    # Clean up test metadata & file
    with pool.lock:
        if unusable_file in pool.metadata.get("files", {}):
            del pool.metadata["files"][unusable_file]
    pool._save_metadata()

    if os.path.exists(active_path):
        try: os.remove(active_path)
        except: pass

if __name__ == "__main__":
    test_unusable_detection()
    test_pool_quarantine_and_exclusion()
    print("ALL UNUSABLE AUDIO DETECTION TESTS PASSED!")

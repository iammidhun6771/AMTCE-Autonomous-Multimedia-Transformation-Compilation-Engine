import os
import sys
import time

repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, repo_root)
sys.path.insert(0, os.path.join(repo_root, "Audio_Modules"))

from lyric_rhythm_aligner import analyze_music

def test_caching():
    target_audio = os.path.join(repo_root, "Original_audio", "cooldown", "Pooja_hedge.mp3")
    if not os.path.exists(target_audio):
        print(f"Target audio missing: {target_audio}")
        return

    print(f"--- 1st Call on '{os.path.basename(target_audio)}' ---")
    t0 = time.time()
    res1 = analyze_music(target_audio)
    t1 = time.time() - t0
    print(f"Call 1 Result: _source='{res1.get('_source')}', emotion='{res1.get('dominant_emotion')}', elapsed={t1:.2f}s")

    print(f"\n--- 2nd Call on '{os.path.basename(target_audio)}' ---")
    t2_start = time.time()
    res2 = analyze_music(target_audio)
    t2 = time.time() - t2_start
    print(f"Call 2 Result: _source='{res2.get('_source')}', emotion='{res2.get('dominant_emotion')}', elapsed={t2:.4f}s")

    assert res2.get("_source") == "cache_hit", "Expected 2nd call to be cache_hit!"
    assert t2 < 0.1, f"Expected 2nd call to be ultra fast (<0.1s), but took {t2:.4f}s!"
    print("\n[SUCCESS] REAL AUDIO CACHING VERIFIED SUCCESSFULLY!")

if __name__ == "__main__":
    test_caching()

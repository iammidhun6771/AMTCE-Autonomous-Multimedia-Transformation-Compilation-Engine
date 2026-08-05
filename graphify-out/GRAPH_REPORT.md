# Graph Report - D:\AMTCE  (2026-08-06)

## Corpus Check
- 125 files · ~417,652 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1319 nodes · 2825 edges · 58 communities detected
- Extraction: 59% EXTRACTED · 41% INFERRED · 0% AMBIGUOUS · INFERRED: 1165 edges (avg confidence: 0.64)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 9|Community 9]]
- [[_COMMUNITY_Community 10|Community 10]]
- [[_COMMUNITY_Community 11|Community 11]]
- [[_COMMUNITY_Community 12|Community 12]]
- [[_COMMUNITY_Community 13|Community 13]]
- [[_COMMUNITY_Community 14|Community 14]]
- [[_COMMUNITY_Community 15|Community 15]]
- [[_COMMUNITY_Community 16|Community 16]]
- [[_COMMUNITY_Community 17|Community 17]]
- [[_COMMUNITY_Community 18|Community 18]]
- [[_COMMUNITY_Community 19|Community 19]]
- [[_COMMUNITY_Community 20|Community 20]]
- [[_COMMUNITY_Community 21|Community 21]]
- [[_COMMUNITY_Community 22|Community 22]]
- [[_COMMUNITY_Community 23|Community 23]]
- [[_COMMUNITY_Community 24|Community 24]]
- [[_COMMUNITY_Community 25|Community 25]]
- [[_COMMUNITY_Community 26|Community 26]]
- [[_COMMUNITY_Community 27|Community 27]]
- [[_COMMUNITY_Community 28|Community 28]]
- [[_COMMUNITY_Community 29|Community 29]]
- [[_COMMUNITY_Community 30|Community 30]]
- [[_COMMUNITY_Community 31|Community 31]]
- [[_COMMUNITY_Community 32|Community 32]]
- [[_COMMUNITY_Community 33|Community 33]]
- [[_COMMUNITY_Community 34|Community 34]]
- [[_COMMUNITY_Community 35|Community 35]]
- [[_COMMUNITY_Community 36|Community 36]]
- [[_COMMUNITY_Community 37|Community 37]]
- [[_COMMUNITY_Community 38|Community 38]]
- [[_COMMUNITY_Community 39|Community 39]]
- [[_COMMUNITY_Community 40|Community 40]]
- [[_COMMUNITY_Community 41|Community 41]]
- [[_COMMUNITY_Community 42|Community 42]]
- [[_COMMUNITY_Community 43|Community 43]]
- [[_COMMUNITY_Community 44|Community 44]]
- [[_COMMUNITY_Community 45|Community 45]]
- [[_COMMUNITY_Community 46|Community 46]]
- [[_COMMUNITY_Community 47|Community 47]]
- [[_COMMUNITY_Community 48|Community 48]]
- [[_COMMUNITY_Community 49|Community 49]]
- [[_COMMUNITY_Community 50|Community 50]]
- [[_COMMUNITY_Community 51|Community 51]]
- [[_COMMUNITY_Community 52|Community 52]]
- [[_COMMUNITY_Community 53|Community 53]]
- [[_COMMUNITY_Community 54|Community 54]]
- [[_COMMUNITY_Community 55|Community 55]]
- [[_COMMUNITY_Community 56|Community 56]]
- [[_COMMUNITY_Community 57|Community 57]]

## God Nodes (most connected - your core abstractions)
1. `get()` - 218 edges
2. `BeatEngine` - 121 edges
3. `AudioPoolManager` - 108 edges
4. `ClipIntelligenceStore` - 102 edges
5. `MasterAIEditor` - 61 edges
6. `PublishQueue` - 55 edges
7. `TelegramVaultIndexer` - 48 edges
8. `GeminiFFmpegEngine` - 40 edges
9. `ImportGate` - 36 edges
10. `FFmpegCommandGenerator` - 33 edges

## Surprising Connections (you probably didn't know these)
- `Plug this family into the AMTCE master orchestration registry.          Future A` --uses--> `BeatEngine`  [INFERRED]
  D:\AMTCE\simpler update\Audio_Modules\audio_family_pipeline.py → D:\AMTCE\simpler update\Audio_Modules\beat_engine.py
- `AudioPoolManager` --uses--> `Publishing_Modules / telegram_vault_indexer.py =================================`  [INFERRED]
  D:\AMTCE\simpler update\Audio_Modules\audio_pool_manager.py → D:\AMTCE\simpler update\Publishing_Modules\telegram_vault_indexer.py
- `AudioPoolManager` --uses--> `Manages reading, writing, uploading, and pinning the master_vault_index.json`  [INFERRED]
  D:\AMTCE\simpler update\Audio_Modules\audio_pool_manager.py → D:\AMTCE\simpler update\Publishing_Modules\telegram_vault_indexer.py
- `AudioPoolManager` --uses--> `Column 2 Lookup: Returns cached raw video file_id and audio_math if this URL`  [INFERRED]
  D:\AMTCE\simpler update\Audio_Modules\audio_pool_manager.py → D:\AMTCE\simpler update\Publishing_Modules\telegram_vault_indexer.py
- `AudioPoolManager` --uses--> `Column 1 Lookup: Returns master reel data and full intelligence dicts by`  [INFERRED]
  D:\AMTCE\simpler update\Audio_Modules\audio_pool_manager.py → D:\AMTCE\simpler update\Publishing_Modules\telegram_vault_indexer.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.02
Nodes (132): Phase_2 / 02_forensic_perception.py ==================================== Step 2:, Executes Gemini Call 1.     Returns result dictionary containing visual_context,, run_forensic_perception(), build_rhythm_timeline(), Phase_2 / 05_rhythm_timeline.py =============================== Step 5: Rhythm &, Builds micro-shots and routing parameters for editing., commit_rag_creator_behavior(), Phase 3 — Step 07: Master RAG Vector Memory Committer ========================== (+124 more)

### Community 1 - "Community 1"
Cohesion: 0.03
Nodes (109): ingest_to_publish_queue(), Phase 3 — Step 01: Queue Ingest Manager ========================================, Ingest a rendered video file into publish_queue.json.      Args:         video_p, Compatibility shim for the sample update tree.  This file provides the local pub, _async_static_scheduler_task(), build_back_button_keyboard(), build_best_attempt_comparison_keyboard(), build_platform_selection_keyboard() (+101 more)

### Community 2 - "Community 2"
Cohesion: 0.03
Nodes (91): Phase_2 / 04_bgm_selector.py ============================ Step 4: Gemini Call 2, Attempts to load a previously selected BGM track from ClipIntelligenceStore., Executes Gemini Call 2 BGM Selector.     Returns dict containing selected_audio_, Executes Gemini Call 2 BGM Selector.      Stage 2 Cache Lock:         If intent_, select_clip_bgm(), _try_load_cached_bgm(), extract_audio(), _has_audio_stream() (+83 more)

### Community 3 - "Community 3"
Cohesion: 0.04
Nodes (43): _is_api_outage_or_key_error(), Phase_2 / 06_ffmpeg_synthesis.py ================================ Step 6: Gemini, Executes Gemini Call 3 to synthesize FFmpeg filtergraph plan.     Falls back to, Executes Gemini Call 3 to synthesize FFmpeg filtergraph plan.     Falls back to, Returns True ONLY IF error is caused by:       - 503 Service Unavailable / Overl, Offline DSP fallback using MusicDrivenEditor & FFmpeg when Gemini Call 3 API is, _run_music_driven_fallback(), synthesize_editing_plan() (+35 more)

### Community 4 - "Community 4"
Cohesion: 0.06
Nodes (83): detect_faces(), FaceProtector, HybridWatermarkDetector, is_safe_region(), load_detected_niche(), _niche_sidecar_path(), Hybrid Watermark Manager (Gemini Authority) -----------------------------------, Logs user feedback (Reinforcement Learning Stub).         In "Strict Mode", thi (+75 more)

### Community 5 - "Community 5"
Cohesion: 0.04
Nodes (80): publish_to_tiktok(), Phase 3 — Step 05: TikTok Publisher ===================================== Handle, Publish video to TikTok platform.      Args:         video_path: Path to rendere, detect_gender_from_name(), _extract_person_name(), get_source_accounts(), _load_identities(), _paparazzi_creds_exist() (+72 more)

### Community 6 - "Community 6"
Cohesion: 0.04
Nodes (60): Phase 3 — Step 02: Monetization & Safety QA Gate ===============================, Verify safety and monetization compliance from clip intelligence.      Args:, verify_monetization_compliance(), generate_publishing_metadata(), Phase 3 — Step 03: Viral Metadata & Caption Generator ==========================, Generate platform-optimized titles, descriptions, and hashtags from intelligence, publish_to_meta(), Phase 3 — Step 04: Meta (Instagram & Facebook Reels) Publisher ================= (+52 more)

### Community 7 - "Community 7"
Cohesion: 0.05
Nodes (32): Uploads audio WAV file to Gemini and sends raw Faster-Whisper transcript, Send keyframes + candidate BGM audio metadata table to Gemini 2.5 Flash Vision., Send frames + micro-crops + prompt to Gemini Vision, parse and validate JSON res, Parse and validate Gemini JSON response.         Handles BOTH schemas:, GeminiGovernor, is_gemini_globally_down(), Check if the global circuit breaker is active., Public wrapper for prompt simplification used by the VANGUARD retry loop. (+24 more)

### Community 8 - "Community 8"
Cohesion: 0.04
Nodes (37): 01_source_config.py — Phase 1 Step 1: Target Source Account & Channel Resolver =, Step 1 Execution: Resolves target accounts to scrape., resolve_target_accounts(), check_deduplication(), 02_dedup_ledger.py — Phase 1 Step 2: Content Deduplication & Disk Checker ======, Step 2 Execution: Verifies if clip shortcode is clean/unique or already on disk., harvest_reels_from_apify(), 03_apify_harvester.py — Phase 1 Step 3: Apify Reel Scraper & Pre-screener ====== (+29 more)

### Community 9 - "Community 9"
Cohesion: 0.06
Nodes (36): Phase_2 / 01_folder_scanner.py ============================== Step 1: Scans `dow, Scans for clip targets. Returns list of target clip dicts:     [{"dir": clip_fol, scan_clip_targets(), extract_targeted_frames(), Phase_2 / 03_vector_frame_extractor.py ====================================== St, Extracts targeted frames using Gemini visual_vectors.     Returns list of absolu, Phase_2 / 07_master_render.py ============================= Step 7: Master FFmpe, Verifies output master reel in Processed Shorts/. (+28 more)

### Community 10 - "Community 10"
Cohesion: 0.08
Nodes (38): apify_get_video_url(), apify_get_video_url_any(), apify_scrape_creator_accounts(), _check_quota(), _consume_quota(), _find_video_urls(), gemini_reel_prescreen(), _get_client() (+30 more)

### Community 11 - "Community 11"
Cohesion: 0.07
Nodes (34): _batch_label(), _detect_gender(), _download_reel(), _extract_person_name(), _fetch_reels_apify(), get_source_accounts(), _inject_niche(), _men_channel() (+26 more)

### Community 12 - "Community 12"
Cohesion: 0.15
Nodes (10): Core_Modules / session_manager.py ================================== Thread-safe, Increments retry_count. Returns (should_retry, new_count).         Caller decide, Records a rendered attempt video path into attempt_history., Record 1-5 star user feedback rating., Record optional e-commerce affiliate link and product MRP/price., Recover active sessions from disk on startup., Thread-safe session store with per-user locking and atomic disk persistence., Context manager to acquire user-level lock and retrieve session. (+2 more)

### Community 13 - "Community 13"
Cohesion: 0.11
Nodes (25): get_all_active_accounts(), get_primary_accounts(), get_secondary_accounts(), _get_social_folders(), get_target_folder(), is_account_mode_enabled(), _load_config(), actress_config.py — AMTCE Actress Account Router ============================== (+17 more)

### Community 14 - "Community 14"
Cohesion: 0.15
Nodes (17): BaseModel, AutoHarvestRequest, ConnectionManager, EventBroadcastRequest, get_status(), ManualHarvestRequest, on_startup(), pipeline_event_callback() (+9 more)

### Community 15 - "Community 15"
Cohesion: 0.12
Nodes (17): encode_proxy_video(), 05_proxy_encoder.py — Phase 1 Step 5: 480p Proxy Video Encoder =================, Step 5 Execution: Encodes 480p proxy video., _extract_shortcode(), downloader_main.py — Standalone Phase 1 Ingestion & Downloader Orchestrator ====, Extracts shortcode/ID from Instagram Reel, YouTube Short, TikTok, or generic URL, Redirects execution to central Import_Modules / Phase_1 orchestrator., run_phase1_ingestion() (+9 more)

### Community 16 - "Community 16"
Cohesion: 0.13
Nodes (13): ClipTranscriber, simpler update / Clip_Transcriber_Module / clip_transcriber.py =================, Standalone Clip Transcriber module integrating Faster-Whisper audio transcriptio, Executes the full pipeline:           1. Extract WAV audio from video clip., Saves results into JSON and TXT format inside the output directory., Helper shortcut function to run clip transcriber on a video file., transcribe_and_enhance_clip(), Phase 3 Package — Master Distribution, Publishing & Creator RAG Feedback ======= (+5 more)

### Community 17 - "Community 17"
Cohesion: 0.14
Nodes (20): check_platform_lock(), _get_service_sync(), get_valid_credentials(), main(), Niche-Aware Credential Resolver.      Resolution order:       1. Niche folder, Retrieves and refreshes valid credentials.     Accepts an optional niche to rou, Checks if the video file has fresh metadata (Unique ID, Creation Time).     Ret, Injects a fresh Unique ID into the video metadata without re-encoding. (+12 more)

### Community 18 - "Community 18"
Cohesion: 0.17
Nodes (14): analyze_scene_pre_pipeline(), cluster_faces(), load_cached_face(), OpenCVFaceDetector, Gemini_Modules/scene_intel.py — Scene & Face Intelligence Layer ================, OpenCV DNN Res10 300x300 Caffe SSD Face Detector with Haar Cascade Fallback., Detect faces in frame.         Returns list of bboxes: [(x, y, w, h), ...], Groups bounding box locations across keyframes into Subject A, B, C... (+6 more)

### Community 19 - "Community 19"
Cohesion: 0.22
Nodes (13): clean_json_response(), detect_watermark(), evaluate(), extract_best_frame_ffmpeg(), frame_to_pil(), Gemini Watermark Detection Module --------------------------------- Isolated m, Detects watermarks AND classifies fashion vs NSFW + picks best thumbnail frame i, Uses ffmpeg to extract the single best frame identified by detect_watermark(). (+5 more)

### Community 20 - "Community 20"
Cohesion: 0.19
Nodes (7): HumanPresenceGuard, Visual Safety & Quality Orchestrator ------------------------------------ Gove, Primary Quality Signal:         Detects if humans are present to GATE risky enh, Primary Quality Signal:         Detects if humans are present to GATE risky enh, Loads OpenCV DNN Face Detector (ResNet-10) with Haar Cascade fallback, Returns list of faces: {'box': [x,y,w,h], 'confidence': float}         STRICT:, Returns list of faces: {'box': [x,y,w,h], 'confidence': float}         STRICT:

### Community 21 - "Community 21"
Cohesion: 0.31
Nodes (4): get_instance(), LamaEngine, Deep Hybrid Inpainting Engine (LaMa Wrapper) ----------------------------------, Deep hallucinates missing pixels inside the mask using LaMa context logic.

### Community 22 - "Community 22"
Cohesion: 0.5
Nodes (4): main(), phase2_1_main.py — Phase 2.1 Watermark Cleanup Gate ===========================, Run the watermark cleanup stage and return the final cleaned video path., run_phase2_1_watermark_gate()

### Community 23 - "Community 23"
Cohesion: 0.5
Nodes (3): notify_tracker(), Import_Modules / tracker_notifier.py ==================================== Lightw, Sends stage event to local tracker server. Safe & non-blocking if server is offl

### Community 24 - "Community 24"
Cohesion: 1.0
Nodes (1): run_transcriber.py — AMTCE Root Transcriber Entrypoint =========================

### Community 25 - "Community 25"
Cohesion: 1.0
Nodes (1): Import_Modules / phase1_imports.py =================================== Centraliz

### Community 26 - "Community 26"
Cohesion: 1.0
Nodes (1): Import_Modules / phase2_imports.py ================================== Central Hu

### Community 27 - "Community 27"
Cohesion: 1.0
Nodes (1): Import Hub for Phase 3 Package ================================ Exposes all Phas

### Community 28 - "Community 28"
Cohesion: 1.0
Nodes (0): 

### Community 29 - "Community 29"
Cohesion: 1.0
Nodes (0): 

### Community 30 - "Community 30"
Cohesion: 1.0
Nodes (0): 

### Community 31 - "Community 31"
Cohesion: 1.0
Nodes (0): 

### Community 32 - "Community 32"
Cohesion: 1.0
Nodes (0): 

### Community 33 - "Community 33"
Cohesion: 1.0
Nodes (1): Resolves Meta credentials using a 3-tier priority chain:           1. Credentia

### Community 34 - "Community 34"
Cohesion: 1.0
Nodes (1): Orchestrates uploads to enabled Meta platforms.          The ``niche`` paramet

### Community 35 - "Community 35"
Cohesion: 1.0
Nodes (1): Uploads the local image to a temporary public host so the Instagram         Gra

### Community 36 - "Community 36"
Cohesion: 1.0
Nodes (1): Smart person-aware Instagram ratio formatter (4:5 = 1080x1350).          Strat

### Community 37 - "Community 37"
Cohesion: 1.0
Nodes (1): Uploads a standard Image Post to Instagram feed using the Graph API.         Re

### Community 38 - "Community 38"
Cohesion: 1.0
Nodes (1): Cleans captions of UTF-16 surrogates that cause UnicodeEncodeError in httpx/UTF-

### Community 39 - "Community 39"
Cohesion: 1.0
Nodes (1): Generic retry wrapper for HTTP requests using httpx.         Default timeout in

### Community 40 - "Community 40"
Cohesion: 1.0
Nodes (1): Polls Instagram container status until FINISHED or ERROR.         Timeout defau

### Community 41 - "Community 41"
Cohesion: 1.0
Nodes (1): Fix C: remove `item` from `container` by object identity, not value         equa

### Community 42 - "Community 42"
Cohesion: 1.0
Nodes (1): Get a module by name, loading it lazily if not already cached.

### Community 43 - "Community 43"
Cohesion: 1.0
Nodes (1): Clear the import cache.

### Community 44 - "Community 44"
Cohesion: 1.0
Nodes (1): Singleton pattern so we only load the 500MB model into memory once.

### Community 45 - "Community 45"
Cohesion: 1.0
Nodes (0): 

### Community 46 - "Community 46"
Cohesion: 1.0
Nodes (0): 

### Community 47 - "Community 47"
Cohesion: 1.0
Nodes (1): Hydrates local disk stores (pool_metadata.json, .clip_intelligence.json)

### Community 48 - "Community 48"
Cohesion: 1.0
Nodes (1): [FIX] Move any loose .mp3/.wav files sitting in Original_audio/ root into

### Community 49 - "Community 49"
Cohesion: 1.0
Nodes (1): Scan active/ folder and ensure all files are registered in pool_metadata.json.

### Community 50 - "Community 50"
Cohesion: 1.0
Nodes (1): Daemon thread: analyze one BGM track with Gemini and write the result         b

### Community 51 - "Community 51"
Cohesion: 1.0
Nodes (1): Lazy load beat data from cache or disk.

### Community 52 - "Community 52"
Cohesion: 1.0
Nodes (1): Moves newly extracted audio into pool and caches deep beat metadata.

### Community 53 - "Community 53"
Cohesion: 1.0
Nodes (1): Rotate files from cooldown back to active. If force=True, recycle all files imme

### Community 54 - "Community 54"
Cohesion: 1.0
Nodes (1): Mark a BGM track as used without moving to cooldown (rotation disabled per direc

### Community 55 - "Community 55"
Cohesion: 1.0
Nodes (1): Rotates clips from cooldown back to active based on hybrid logic.         Clean

### Community 56 - "Community 56"
Cohesion: 1.0
Nodes (1): Return the pool_metadata["files"] dict — the unified audio track index.

### Community 57 - "Community 57"
Cohesion: 1.0
Nodes (1): Merge rich lyric intelligence fields from a _lyric.json result INTO         poo

## Knowledge Gaps
- **343 isolated node(s):** `phase2_1_main.py — Phase 2.1 Watermark Cleanup Gate ===========================`, `Run the watermark cleanup stage and return the final cleaned video path.`, `Delegates Phase 2 Master AI Editing Pipeline to Phase_2.phase2_orchestrator.`, `Resolve ffmpeg binary path. Checks PATH first, then common install locations.`, `Encode a raw video to a 480p H.264 proxy for Gemini vision analysis.      Args:` (+338 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 24`** (2 nodes): `run_transcriber.py`, `run_transcriber.py — AMTCE Root Transcriber Entrypoint =========================`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 25`** (2 nodes): `phase1_imports.py`, `Import_Modules / phase1_imports.py =================================== Centraliz`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 26`** (2 nodes): `phase2_imports.py`, `Import_Modules / phase2_imports.py ================================== Central Hu`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 27`** (2 nodes): `phase3_imports.py`, `Import Hub for Phase 3 Package ================================ Exposes all Phas`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 28`** (1 nodes): `check_yaml.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 29`** (1 nodes): `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 30`** (1 nodes): `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 31`** (1 nodes): `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 32`** (1 nodes): `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 33`** (1 nodes): `Resolves Meta credentials using a 3-tier priority chain:           1. Credentia`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 34`** (1 nodes): `Orchestrates uploads to enabled Meta platforms.          The ``niche`` paramet`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 35`** (1 nodes): `Uploads the local image to a temporary public host so the Instagram         Gra`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 36`** (1 nodes): `Smart person-aware Instagram ratio formatter (4:5 = 1080x1350).          Strat`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 37`** (1 nodes): `Uploads a standard Image Post to Instagram feed using the Graph API.         Re`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 38`** (1 nodes): `Cleans captions of UTF-16 surrogates that cause UnicodeEncodeError in httpx/UTF-`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 39`** (1 nodes): `Generic retry wrapper for HTTP requests using httpx.         Default timeout in`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 40`** (1 nodes): `Polls Instagram container status until FINISHED or ERROR.         Timeout defau`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 41`** (1 nodes): `Fix C: remove `item` from `container` by object identity, not value         equa`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 42`** (1 nodes): `Get a module by name, loading it lazily if not already cached.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 43`** (1 nodes): `Clear the import cache.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 44`** (1 nodes): `Singleton pattern so we only load the 500MB model into memory once.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 45`** (1 nodes): `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 46`** (1 nodes): `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 47`** (1 nodes): `Hydrates local disk stores (pool_metadata.json, .clip_intelligence.json)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 48`** (1 nodes): `[FIX] Move any loose .mp3/.wav files sitting in Original_audio/ root into`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 49`** (1 nodes): `Scan active/ folder and ensure all files are registered in pool_metadata.json.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 50`** (1 nodes): `Daemon thread: analyze one BGM track with Gemini and write the result         b`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 51`** (1 nodes): `Lazy load beat data from cache or disk.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 52`** (1 nodes): `Moves newly extracted audio into pool and caches deep beat metadata.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 53`** (1 nodes): `Rotate files from cooldown back to active. If force=True, recycle all files imme`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 54`** (1 nodes): `Mark a BGM track as used without moving to cooldown (rotation disabled per direc`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 55`** (1 nodes): `Rotates clips from cooldown back to active based on hybrid logic.         Clean`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 56`** (1 nodes): `Return the pool_metadata["files"] dict — the unified audio track index.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 57`** (1 nodes): `Merge rich lyric intelligence fields from a _lyric.json result INTO         poo`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `get()` connect `Community 5` to `Community 0`, `Community 1`, `Community 2`, `Community 3`, `Community 4`, `Community 6`, `Community 7`, `Community 8`, `Community 9`, `Community 10`, `Community 11`, `Community 13`, `Community 14`, `Community 15`, `Community 16`, `Community 17`, `Community 18`, `Community 19`?**
  _High betweenness centrality (0.592) - this node is a cross-community bridge._
- **Why does `ClipIntelligenceStore` connect `Community 0` to `Community 1`, `Community 2`, `Community 3`, `Community 7`?**
  _High betweenness centrality (0.074) - this node is a cross-community bridge._
- **Why does `MasterAIEditor` connect `Community 1` to `Community 0`, `Community 2`, `Community 3`?**
  _High betweenness centrality (0.064) - this node is a cross-community bridge._
- **Are the 216 inferred relationships involving `get()` (e.g. with `.process()` and `main()`) actually correct?**
  _`get()` has 216 INFERRED edges - model-reasoned connections that need verification._
- **Are the 111 inferred relationships involving `BeatEngine` (e.g. with `MasterAIEditor` and `master_ai_editor.py — End-to-End AI Video Editor Engine ========================`) actually correct?**
  _`BeatEngine` has 111 INFERRED edges - model-reasoned connections that need verification._
- **Are the 87 inferred relationships involving `AudioPoolManager` (e.g. with `MasterAIEditor` and `master_ai_editor.py — End-to-End AI Video Editor Engine ========================`) actually correct?**
  _`AudioPoolManager` has 87 INFERRED edges - model-reasoned connections that need verification._
- **Are the 83 inferred relationships involving `ClipIntelligenceStore` (e.g. with `Core_Modules / purger.py ======================= Complete Clip & Asset Purger. W` and `Completely purges a clip and all related assets:       - Master rendered video (`) actually correct?**
  _`ClipIntelligenceStore` has 83 INFERRED edges - model-reasoned connections that need verification._
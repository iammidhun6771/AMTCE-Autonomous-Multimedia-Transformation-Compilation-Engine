# Graph Report - D:\AMTCE  (2026-08-05)

## Corpus Check
- 123 files · ~401,902 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1194 nodes · 2556 edges · 49 communities detected
- Extraction: 63% EXTRACTED · 37% INFERRED · 0% AMBIGUOUS · INFERRED: 957 edges (avg confidence: 0.67)
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

## God Nodes (most connected - your core abstractions)
1. `get()` - 207 edges
2. `BeatEngine` - 111 edges
3. `ClipIntelligenceStore` - 81 edges
4. `AudioPoolManager` - 64 edges
5. `GeminiFFmpegEngine` - 39 edges
6. `FFmpegCommandGenerator` - 33 edges
7. `ImportGate` - 33 edges
8. `MasterAIEditor` - 31 edges
9. `download_video()` - 26 edges
10. `GeminiGovernor` - 26 edges

## Surprising Connections (you probably didn't know these)
- `audio_extractor.py — Phase 1 Audio Extraction + Beat Analysis ==================` --uses--> `AudioPoolManager`  [INFERRED]
  D:\AMTCE\simpler update\Audio_Modules\audio_extractor.py → D:\AMTCE\simpler update\Audio_Modules\audio_pool_manager.py
- `Returns True if the file has at least one audio stream (fast ffprobe check).` --uses--> `AudioPoolManager`  [INFERRED]
  D:\AMTCE\simpler update\Audio_Modules\audio_extractor.py → D:\AMTCE\simpler update\Audio_Modules\audio_pool_manager.py
- `Extracts mono 16 kHz PCM WAV from video_path → output_path.     Returns True on` --uses--> `AudioPoolManager`  [INFERRED]
  D:\AMTCE\simpler update\Audio_Modules\audio_extractor.py → D:\AMTCE\simpler update\Audio_Modules\audio_pool_manager.py
- `Ingests clean musical audio extracted from a Phase 1 clip into the central     O` --uses--> `AudioPoolManager`  [INFERRED]
  D:\AMTCE\simpler update\Audio_Modules\audio_extractor.py → D:\AMTCE\simpler update\Audio_Modules\audio_pool_manager.py
- `Phase 2 helper: loads pre-computed audio_analysis.json from clip_dir.     Return` --uses--> `AudioPoolManager`  [INFERRED]
  D:\AMTCE\simpler update\Audio_Modules\audio_extractor.py → D:\AMTCE\simpler update\Audio_Modules\audio_pool_manager.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.03
Nodes (102): ingest_to_publish_queue(), Phase 3 — Step 01: Queue Ingest Manager ========================================, Ingest a rendered video file into publish_queue.json.      Args:         video_p, Phase 3 — Step 02: Monetization & Safety QA Gate ===============================, Verify safety and monetization compliance from clip intelligence.      Args:, verify_monetization_compliance(), generate_publishing_metadata(), Phase 3 — Step 03: Viral Metadata & Caption Generator ========================== (+94 more)

### Community 1 - "Community 1"
Cohesion: 0.04
Nodes (52): _is_api_outage_or_key_error(), Phase_2 / 06_ffmpeg_synthesis.py ================================ Step 6: Gemini, Executes Gemini Call 3 to synthesize FFmpeg filtergraph plan.     Falls back to, Returns True ONLY IF error is caused by:       - 503 Service Unavailable / Overl, Offline DSP fallback using MusicDrivenEditor & FFmpeg when Gemini Call 3 API is, _run_music_driven_fallback(), synthesize_editing_plan(), cmd_list_to_string() (+44 more)

### Community 2 - "Community 2"
Cohesion: 0.04
Nodes (63): Phase_2 / 04_bgm_selector.py ============================ Step 4: Gemini Call 2, Executes Gemini Call 2 BGM Selector.     Returns dict containing selected_audio_, select_clip_bgm(), Phase 1 post-download hook. Called immediately after video.mp4 is saved.      St, run_phase1_audio_analysis(), AudioFamilyPipeline, _empty_packet(), AudioFamilyPipeline v2.0 — "Saints With Ego" =================================== (+55 more)

### Community 3 - "Community 3"
Cohesion: 0.06
Nodes (81): detect_faces(), FaceProtector, HybridWatermarkDetector, is_safe_region(), load_detected_niche(), _niche_sidecar_path(), Hybrid Watermark Manager (Gemini Authority) -----------------------------------, Logs user feedback (Reinforcement Learning Stub).         In "Strict Mode", thi (+73 more)

### Community 4 - "Community 4"
Cohesion: 0.04
Nodes (51): commit_rag_creator_behavior(), Phase 3 — Step 07: Master RAG Vector Memory Committer ==========================, Commit final clip intelligence & publishing results to master RAG store.      Ar, load_audio_analysis(), Phase 2 helper: loads pre-computed audio_analysis.json from clip_dir.     Return, ClipIntelligenceStore, Gemini_Modules/clip_intelligence_store.py ======================================, Returns a blank clip intelligence record with correct schema. (+43 more)

### Community 5 - "Community 5"
Cohesion: 0.04
Nodes (68): Plug this family into the AMTCE master orchestration registry.          Future A, Analyze beats on the BGM (preferred) or extracted WAV (fallback).          What, If the pool selected a DIFFERENT BGM than the initial hint, re-run         beat_, analyze_beats_with_drops(), BeatEngine, get_beats(), get_beats_preferring_original_audio(), get_beats_with_drops() (+60 more)

### Community 6 - "Community 6"
Cohesion: 0.05
Nodes (60): _async_static_scheduler_task(), build_back_button_keyboard(), build_best_attempt_comparison_keyboard(), build_platform_selection_keyboard(), build_reedit_options_keyboard(), build_telegram_session_keyboard(), cmd_ytcode(), execute_reedit_with_directive() (+52 more)

### Community 7 - "Community 7"
Cohesion: 0.05
Nodes (36): Phase_2 / 01_folder_scanner.py ============================== Step 1: Scans `dow, Scans for clip targets. Returns list of target clip dicts:     [{"dir": clip_fol, scan_clip_targets(), Phase_2 / 02_forensic_perception.py ==================================== Step 2:, Executes Gemini Call 1.     Returns result dictionary containing visual_context,, run_forensic_perception(), build_rhythm_timeline(), Phase_2 / 05_rhythm_timeline.py =============================== Step 5: Rhythm & (+28 more)

### Community 8 - "Community 8"
Cohesion: 0.06
Nodes (40): check_deduplication(), 02_dedup_ledger.py — Phase 1 Step 2: Content Deduplication & Disk Checker ======, Step 2 Execution: Verifies if clip shortcode is clean/unique or already on disk., apify_get_video_url(), apify_get_video_url_any(), apify_scrape_creator_accounts(), _check_quota(), _consume_quota() (+32 more)

### Community 9 - "Community 9"
Cohesion: 0.05
Nodes (35): 01_source_config.py — Phase 1 Step 1: Target Source Account & Channel Resolver =, Step 1 Execution: Resolves target accounts to scrape., resolve_target_accounts(), harvest_reels_from_apify(), 03_apify_harvester.py — Phase 1 Step 3: Apify Reel Scraper & Pre-screener ======, Step 3 Execution: Scrapes target reels via Apify actor., download_stream(), 04_core_downloader.py — Phase 1 Step 4: Multi-Platform Stream Downloader ======= (+27 more)

### Community 10 - "Community 10"
Cohesion: 0.07
Nodes (17): GeminiGovernor, is_gemini_globally_down(), Check if the global circuit breaker is active., Public wrapper for prompt simplification used by the VANGUARD retry loop., Record a 5xx failure. Trip breaker if conditions met., [VANGUARD] Local Fallback to Ollama (Phi-3)., VANGUARD BULLETPROOF GENERATOR: Loop-based Retry + Global Deadline + Jitter., Reset the circuit breaker on a successful call. (+9 more)

### Community 11 - "Community 11"
Cohesion: 0.07
Nodes (36): _batch_label(), _detect_gender(), _download_reel(), _extract_person_name(), _fetch_reels_apify(), get_source_accounts(), _inject_niche(), _men_channel() (+28 more)

### Community 12 - "Community 12"
Cohesion: 0.08
Nodes (20): ClipTranscriber, simpler update / Clip_Transcriber_Module / clip_transcriber.py =================, Standalone Clip Transcriber module integrating Faster-Whisper audio transcriptio, Executes the full pipeline:           1. Extract WAV audio from video clip., Uploads audio WAV file to Gemini and sends raw Faster-Whisper transcript, Saves results into JSON and TXT format inside the output directory., Helper shortcut function to run clip transcriber on a video file., transcribe_and_enhance_clip() (+12 more)

### Community 13 - "Community 13"
Cohesion: 0.15
Nodes (10): Core_Modules / session_manager.py ================================== Thread-safe, Increments retry_count. Returns (should_retry, new_count).         Caller decide, Records a rendered attempt video path into attempt_history., Record 1-5 star user feedback rating., Record optional e-commerce affiliate link and product MRP/price., Recover active sessions from disk on startup., Thread-safe session store with per-user locking and atomic disk persistence., Context manager to acquire user-level lock and retrieve session. (+2 more)

### Community 14 - "Community 14"
Cohesion: 0.12
Nodes (24): extract_targeted_frames(), Phase_2 / 03_vector_frame_extractor.py ====================================== St, Extracts targeted frames using Gemini visual_vectors.     Returns list of absolu, _compute_optical_flow_scores(), _detect_scene_cuts(), extract_frames_from_vectors(), extract_high_gradient_crops(), extract_strategic_frame_files() (+16 more)

### Community 15 - "Community 15"
Cohesion: 0.11
Nodes (25): get_all_active_accounts(), get_primary_accounts(), get_secondary_accounts(), _get_social_folders(), get_target_folder(), is_account_mode_enabled(), _load_config(), actress_config.py — AMTCE Actress Account Router ============================== (+17 more)

### Community 16 - "Community 16"
Cohesion: 0.15
Nodes (17): BaseModel, AutoHarvestRequest, ConnectionManager, EventBroadcastRequest, get_status(), ManualHarvestRequest, on_startup(), pipeline_event_callback() (+9 more)

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
Cohesion: 0.21
Nodes (13): detect_gender_from_name(), _extract_person_name(), get_source_accounts(), _load_identities(), _paparazzi_creds_exist(), channel_router.py — AMTCE Paparazzi Channel Router ============================, Returns the list of paparazzi Instagram account IDs to scrape from.     Reads f, Detects gender from a person's name string.     Uses curated token lists from p (+5 more)

### Community 21 - "Community 21"
Cohesion: 0.19
Nodes (7): HumanPresenceGuard, Visual Safety & Quality Orchestrator ------------------------------------ Gove, Primary Quality Signal:         Detects if humans are present to GATE risky enh, Primary Quality Signal:         Detects if humans are present to GATE risky enh, Loads OpenCV DNN Face Detector (ResNet-10) with Haar Cascade fallback, Returns list of faces: {'box': [x,y,w,h], 'confidence': float}         STRICT:, Returns list of faces: {'box': [x,y,w,h], 'confidence': float}         STRICT:

### Community 22 - "Community 22"
Cohesion: 0.36
Nodes (9): authenticate(), _fallback_url_flow(), _get_telegram_creds(), _load_client_secret(), Google Device Authorization Grant.     Requires app type = 'TV and Limited Inpu, Used when device flow is unavailable (app type = Desktop)., Returns (bot_token, admin_private_chat_id).     ALWAYS sends to the ADMIN's pri, _send_telegram() (+1 more)

### Community 23 - "Community 23"
Cohesion: 0.31
Nodes (4): get_instance(), LamaEngine, Deep Hybrid Inpainting Engine (LaMa Wrapper) ----------------------------------, Deep hallucinates missing pixels inside the mask using LaMa context logic.

### Community 24 - "Community 24"
Cohesion: 0.5
Nodes (4): main(), phase2_1_main.py — Phase 2.1 Watermark Cleanup Gate ===========================, Run the watermark cleanup stage and return the final cleaned video path., run_phase2_1_watermark_gate()

### Community 25 - "Community 25"
Cohesion: 0.5
Nodes (3): notify_tracker(), Import_Modules / tracker_notifier.py ==================================== Lightw, Sends stage event to local tracker server. Safe & non-blocking if server is offl

### Community 26 - "Community 26"
Cohesion: 1.0
Nodes (1): run_transcriber.py — AMTCE Root Transcriber Entrypoint =========================

### Community 27 - "Community 27"
Cohesion: 1.0
Nodes (1): Import_Modules / phase1_imports.py =================================== Centraliz

### Community 28 - "Community 28"
Cohesion: 1.0
Nodes (1): Import_Modules / phase2_imports.py ================================== Central Hu

### Community 29 - "Community 29"
Cohesion: 1.0
Nodes (1): Import Hub for Phase 3 Package ================================ Exposes all Phas

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
Nodes (0): 

### Community 34 - "Community 34"
Cohesion: 1.0
Nodes (0): 

### Community 35 - "Community 35"
Cohesion: 1.0
Nodes (1): Resolves Meta credentials using a 3-tier priority chain:           1. Credentia

### Community 36 - "Community 36"
Cohesion: 1.0
Nodes (1): Orchestrates uploads to enabled Meta platforms.          The ``niche`` paramet

### Community 37 - "Community 37"
Cohesion: 1.0
Nodes (1): Uploads the local image to a temporary public host so the Instagram         Gra

### Community 38 - "Community 38"
Cohesion: 1.0
Nodes (1): Smart person-aware Instagram ratio formatter (4:5 = 1080x1350).          Strat

### Community 39 - "Community 39"
Cohesion: 1.0
Nodes (1): Uploads a standard Image Post to Instagram feed using the Graph API.         Re

### Community 40 - "Community 40"
Cohesion: 1.0
Nodes (1): Cleans captions of UTF-16 surrogates that cause UnicodeEncodeError in httpx/UTF-

### Community 41 - "Community 41"
Cohesion: 1.0
Nodes (1): Generic retry wrapper for HTTP requests using httpx.         Default timeout in

### Community 42 - "Community 42"
Cohesion: 1.0
Nodes (1): Polls Instagram container status until FINISHED or ERROR.         Timeout defau

### Community 43 - "Community 43"
Cohesion: 1.0
Nodes (1): Fix C: remove `item` from `container` by object identity, not value         equa

### Community 44 - "Community 44"
Cohesion: 1.0
Nodes (1): Get a module by name, loading it lazily if not already cached.

### Community 45 - "Community 45"
Cohesion: 1.0
Nodes (1): Clear the import cache.

### Community 46 - "Community 46"
Cohesion: 1.0
Nodes (1): Singleton pattern so we only load the 500MB model into memory once.

### Community 47 - "Community 47"
Cohesion: 1.0
Nodes (0): 

### Community 48 - "Community 48"
Cohesion: 1.0
Nodes (0): 

## Knowledge Gaps
- **304 isolated node(s):** `phase2_1_main.py — Phase 2.1 Watermark Cleanup Gate ===========================`, `Run the watermark cleanup stage and return the final cleaned video path.`, `Delegates Phase 2 Master AI Editing Pipeline to Phase_2.phase2_orchestrator.`, `Resolve ffmpeg binary path. Checks PATH first, then common install locations.`, `Encode a raw video to a 480p H.264 proxy for Gemini vision analysis.      Args:` (+299 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 26`** (2 nodes): `run_transcriber.py`, `run_transcriber.py — AMTCE Root Transcriber Entrypoint =========================`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 27`** (2 nodes): `phase1_imports.py`, `Import_Modules / phase1_imports.py =================================== Centraliz`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 28`** (2 nodes): `phase2_imports.py`, `Import_Modules / phase2_imports.py ================================== Central Hu`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 29`** (2 nodes): `phase3_imports.py`, `Import Hub for Phase 3 Package ================================ Exposes all Phas`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 30`** (1 nodes): `check_yaml.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 31`** (1 nodes): `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 32`** (1 nodes): `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 33`** (1 nodes): `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 34`** (1 nodes): `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 35`** (1 nodes): `Resolves Meta credentials using a 3-tier priority chain:           1. Credentia`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 36`** (1 nodes): `Orchestrates uploads to enabled Meta platforms.          The ``niche`` paramet`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 37`** (1 nodes): `Uploads the local image to a temporary public host so the Instagram         Gra`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 38`** (1 nodes): `Smart person-aware Instagram ratio formatter (4:5 = 1080x1350).          Strat`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 39`** (1 nodes): `Uploads a standard Image Post to Instagram feed using the Graph API.         Re`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 40`** (1 nodes): `Cleans captions of UTF-16 surrogates that cause UnicodeEncodeError in httpx/UTF-`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 41`** (1 nodes): `Generic retry wrapper for HTTP requests using httpx.         Default timeout in`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 42`** (1 nodes): `Polls Instagram container status until FINISHED or ERROR.         Timeout defau`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 43`** (1 nodes): `Fix C: remove `item` from `container` by object identity, not value         equa`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 44`** (1 nodes): `Get a module by name, loading it lazily if not already cached.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 45`** (1 nodes): `Clear the import cache.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 46`** (1 nodes): `Singleton pattern so we only load the 500MB model into memory once.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 47`** (1 nodes): `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 48`** (1 nodes): `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `get()` connect `Community 0` to `Community 1`, `Community 2`, `Community 3`, `Community 4`, `Community 5`, `Community 6`, `Community 7`, `Community 8`, `Community 9`, `Community 10`, `Community 11`, `Community 12`, `Community 14`, `Community 15`, `Community 16`, `Community 17`, `Community 18`, `Community 19`, `Community 20`, `Community 22`?**
  _High betweenness centrality (0.695) - this node is a cross-community bridge._
- **Why does `BeatEngine` connect `Community 5` to `Community 0`, `Community 1`, `Community 2`, `Community 4`, `Community 6`, `Community 7`?**
  _High betweenness centrality (0.077) - this node is a cross-community bridge._
- **Why does `_upload_sync()` connect `Community 17` to `Community 0`?**
  _High betweenness centrality (0.048) - this node is a cross-community bridge._
- **Are the 205 inferred relationships involving `get()` (e.g. with `.process()` and `main()`) actually correct?**
  _`get()` has 205 INFERRED edges - model-reasoned connections that need verification._
- **Are the 101 inferred relationships involving `BeatEngine` (e.g. with `MasterAIEditor` and `master_ai_editor.py — End-to-End AI Video Editor Engine ========================`) actually correct?**
  _`BeatEngine` has 101 INFERRED edges - model-reasoned connections that need verification._
- **Are the 62 inferred relationships involving `ClipIntelligenceStore` (e.g. with `Core_Modules / purger.py ======================= Complete Clip & Asset Purger. W` and `Completely purges a clip and all related assets:       - Master rendered video (`) actually correct?**
  _`ClipIntelligenceStore` has 62 INFERRED edges - model-reasoned connections that need verification._
- **Are the 44 inferred relationships involving `AudioPoolManager` (e.g. with `MasterAIEditor` and `master_ai_editor.py — End-to-End AI Video Editor Engine ========================`) actually correct?**
  _`AudioPoolManager` has 44 INFERRED edges - model-reasoned connections that need verification._
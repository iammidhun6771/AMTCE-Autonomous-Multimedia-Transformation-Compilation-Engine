"""
media_publisher_main.py — Phase 4 Standalone Multi-Platform Publishing Orchestrator
=====================================================================================
Orchestrates sequential 4-platform broadcasting for approved master video reels:
  1. YouTube Shorts   (via uploader.py)
  2. Instagram Reels  (via meta_uploader.py)
  3. TikTok Creator   (via tiktok_uploader.py)
  4. Telegram Channel (via Bot API)

Called directly after a user approves a reel title or taps 'Post Immediately' in Telegram.
"""

import os
import sys
import time
import json
import logging
import asyncio
from typing import Dict, Any, Optional

logger = logging.getLogger("media_publisher_main")
logger.setLevel(logging.INFO)

_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# If we're in "simpler update", go up one more level to get to actual AMTCE root
if os.path.basename(_REPO_ROOT) == "simpler update":
    _REPO_ROOT = os.path.dirname(_REPO_ROOT)
    
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

try:
    from dotenv import load_dotenv
    load_dotenv(os.path.join(_REPO_ROOT, ".env"), override=False)
    load_dotenv(os.path.join(_REPO_ROOT, "Credentials", ".env"), override=False)
except ImportError:
    pass


def publish_to_youtube(video_path: str, title: str, description: str = "", tags: str = "", niche: Optional[str] = None) -> Dict[str, Any]:
    """Uploads video reel to YouTube Shorts via YouTube Data API v3."""
    logger.info("🔴 [PUBLISHER 1/4] Uploading to YouTube Shorts...")
    try:
        from Publishing_Modules.uploader import _upload_sync
        cred_file = os.getenv("CLIENT_SECRET_FILE", os.path.join(_REPO_ROOT, "Credentials", "youtube", "client_secret.json"))
        if not os.path.exists(cred_file):
            fallback_cred = os.path.join(_REPO_ROOT, "Credentials", "client_secret.json")
            if os.path.exists(fallback_cred):
                cred_file = fallback_cred

        token_file = os.getenv("YOUTUBE_TOKEN_FILE", os.path.join(_REPO_ROOT, "Credentials", "youtube", "token.json"))
        if not os.path.exists(token_file):
            fallback_token = os.path.join(_REPO_ROOT, "Credentials", "token.json")
            if os.path.exists(fallback_token):
                token_file = fallback_token

        if not os.path.exists(cred_file) and not os.path.exists(token_file):
            logger.warning("⚠️ YouTube API credentials missing (Credentials/youtube/client_secret.json or token.json not found). Skipping YouTube upload.")
            logger.info("💡 To enable YouTube upload, run: python scripts/auth_youtube.py --secret Credentials/youtube/client_secret.json --token Credentials/youtube/token.json --admin-id YOUR_TELEGRAM_ID")
            logger.info("   Then send the localhost link to your Telegram chat with /ytcode {link} to complete authentication.")
            return {"status": "skipped", "message": "Credentials/token.json missing"}

        video_id = _upload_sync(
            file_path=video_path,
            title=title,
            description=description or f"{title}\n\n#shorts #viral #trending",
            hashtags=tags or "#shorts #viral #trending",
            privacy="public",
            niche=niche
        )
        if video_id:
            logger.info("✅ [YOUTUBE SUCCESS] Video ID: %s", video_id)
            return {"status": "success", "video_id": video_id, "url": f"https://youtu.be/{video_id}"}
        else:
            logger.warning("⚠️ YouTube upload completed without returning Video ID.")
            return {"status": "failed", "message": "No video ID returned (possible rate limit or lock)"}
    except Exception as e:
        logger.error("❌ [YOUTUBE ERROR] %s", e)
        return {"status": "failed", "error": str(e)}


async def publish_to_instagram(video_path: str, caption: str, niche: Optional[str] = None) -> Dict[str, Any]:
    """Uploads video reel to Instagram via Meta Graph API."""
    logger.info("📸 [PUBLISHER 2/4] Uploading to Instagram Reels...")
    try:
        from Publishing_Modules.meta_uploader import AsyncMetaUploader
        token = os.getenv("IG_BUSINESS_TOKEN") or os.getenv("META_PAGE_TOKEN")
        ig_user_id = os.getenv("IG_BUSINESS_ACCOUNT_ID") or os.getenv("IG_BUSINESS_ID") or os.getenv("META_IG_ACCOUNT_ID") or os.getenv("META_PAGE_ID")

        if not token or not ig_user_id:
            logger.warning("⚠️ Instagram Graph API credentials missing (IG_BUSINESS_TOKEN / IG_BUSINESS_ACCOUNT_ID). Skipping Instagram upload.")
            return {"status": "skipped", "message": "IG_BUSINESS_TOKEN / Account ID missing in .env"}

        uploader = AsyncMetaUploader()
        res = await uploader.upload_to_meta(
            video_path=video_path,
            caption=caption,
            upload_type="Reels",
            niche=niche or "General_Fallback"
        )
        
        # upload_to_meta returns {"instagram": {...}, "facebook": {...}}
        ig_result = res.get("instagram", {})
        if ig_result.get("status") == "success":
            media_id = ig_result.get("id")
            link = ig_result.get("link", "")
            logger.info("✅ [INSTAGRAM SUCCESS] Media ID: %s, Link: %s", media_id, link)
            return {"status": "success", "media_id": media_id, "link": link}
        else:
            logger.warning("⚠️ Instagram upload failed: %s", ig_result.get("status"))
            return {"status": "failed", "response": res}
    except Exception as e:
        logger.error("❌ [INSTAGRAM ERROR] %s", e)
        return {"status": "failed", "error": str(e)}


async def publish_to_tiktok(video_path: str, title: str, tags: str = "", niche: Optional[str] = None) -> Dict[str, Any]:
    """Uploads video reel to TikTok Creator account via TikTok Direct Post API."""
    logger.info("🎵 [PUBLISHER 3/4] Uploading to TikTok...")
    try:
        from Publishing_Modules.tiktok_uploader import upload_to_tiktok
        res = await upload_to_tiktok(
            file_path=video_path,
            title=title,
            hashtags=tags or "#viral #shorts #trending",
            niche=niche
        )
        if res.get("status") == "success":
            logger.info("✅ [TIKTOK SUCCESS] Publish ID: %s", res.get("id"))
            return {"status": "success", "publish_id": res.get("id")}
        else:
            logger.warning("⚠️ TikTok upload skipped or failed: %s", res.get("error"))
            return {"status": res.get("status", "failed"), "message": res.get("error")}
    except Exception as e:
        logger.error("❌ [TIKTOK ERROR] %s", e)
        return {"status": "failed", "error": str(e)}


async def publish_to_telegram(video_path: str, title: str, caption: str = "") -> Dict[str, Any]:
    """Dispatches published master reel to Telegram Storage Group & Target Chat."""
    logger.info("✈️ [PUBLISHER 4/4] Publishing to Telegram Channel / Group...")
    try:
        from telegram import Bot
        from telegram.request import HTTPXRequest

        bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
        chat_id = os.getenv("TELEGRAM_CHAT_ID") or os.getenv("TELEGRAM_STORAGE_GROUP_ID")
        storage_group = os.getenv("TELEGRAM_STORAGE_GROUP_ID")
        public_group = os.getenv("TELEGRAM_PUBLIC_GROUP_ID")

        if not bot_token:
            logger.warning("⚠️ Telegram Bot Token missing. Skipping Telegram broadcast.")
            return {"status": "skipped", "message": "Bot token missing"}

        # If no primary chat_id, try to use public_group or storage_group as fallback
        if not chat_id:
            if public_group:
                chat_id = public_group
                logger.info("📢 Using TELEGRAM_PUBLIC_GROUP_ID as primary chat since TELEGRAM_CHAT_ID not set")
            elif storage_group:
                chat_id = storage_group
                logger.info("📦 Using TELEGRAM_STORAGE_GROUP_ID as primary chat since TELEGRAM_CHAT_ID not set")
            else:
                logger.warning("⚠️ No Telegram Chat ID configured (TELEGRAM_CHAT_ID, TELEGRAM_PUBLIC_GROUP_ID, or TELEGRAM_STORAGE_GROUP_ID). Skipping Telegram broadcast.")
                return {"status": "skipped", "message": "No chat ID configured"}

        req = HTTPXRequest(connection_pool_size=8, read_timeout=300.0, write_timeout=300.0)
        bot = Bot(token=bot_token, request=req)

        full_caption = f"🚀 **[PUBLISHED MULTI-PLATFORM]**\n📌 **Title**: `{title}`\n📁 `{os.path.basename(video_path)}`"
        if caption:
            full_caption += f"\n\n{caption}"

        with open(video_path, "rb") as vf:
            try:
                sent_msg = await bot.send_video(
                    chat_id=int(chat_id),
                    video=vf,
                    caption=full_caption
                )
            except Exception as send_err:
                error_str = str(send_err)
                if "Forbidden" in error_str or "can't initiate conversation" in error_str.lower():
                    logger.warning(f"⚠️ Cannot send to chat ID {chat_id}: Bot cannot initiate conversation with user. The user must start a conversation with the bot first (send /start), or use a group/channel ID instead.")
                    return {"status": "failed", "error": f"Bot cannot initiate conversation with user {chat_id}. User must message bot first or use group/channel ID."}
                raise

        # Dispatch to Public Telegram Channel / Group if configured
        if public_group:
            try:
                with open(video_path, "rb") as pvf:
                    await bot.send_video(
                        chat_id=int(public_group) if (public_group.startswith("-") or public_group.isdigit()) else public_group,
                        video=pvf,
                        caption=f"🔥 **{title}**\n\n{caption or ''}"
                    )
                logger.info("📢 Dispatched approved reel to Public Telegram Group (%s)", public_group)
            except Exception as pg_e:
                logger.warning("⚠️ Public Telegram Group upload warning: %s", pg_e)

        if storage_group and str(chat_id) != str(storage_group):
            try:
                with open(video_path, "rb") as svf:
                    await bot.send_video(
                        chat_id=int(storage_group),
                        video=svf,
                        caption=f"📦 **[VAULT PUBLISHED BACKUP]**\n📌 `{title}`\n📁 `{os.path.basename(video_path)}`"
                    )
            except Exception as sg_e:
                # More specific error handling for chat not found
                if "Chat not found" in str(sg_e) or "chat not found" in str(sg_e).lower():
                    logger.warning("⚠️ Vault storage group backup skipped: Storage group chat not found. Check TELEGRAM_STORAGE_GROUP_ID in .env")
                else:
                    logger.warning("⚠️ Vault storage group backup warning: %s", sg_e)

        logger.info("✅ [TELEGRAM SUCCESS] Message ID: %s", sent_msg.message_id if sent_msg else "ok")
        return {"status": "success", "message_id": sent_msg.message_id if sent_msg else None}
    except Exception as e:
        logger.error("❌ [TELEGRAM ERROR] %s", e)
        return {"status": "failed", "error": str(e)}


async def run_phase4_publishing_async(
    video_path: str,
    title: str,
    description: str = "",
    tags: str = "#viral #shorts #trending",
    niche: Optional[str] = None
) -> Dict[str, Any]:
    """Async implementation of Phase 4 Multi-Platform Publishing."""
    logger.info("==================================================================")
    logger.info("🚀 [PHASE 4 MEDIA PUBLISHER] Starting Multi-Platform Publishing Workflow")
    logger.info("📌 Reel: %s", os.path.basename(video_path))
    logger.info("📌 Title: '%s'", title)
    logger.info("==================================================================")

    if not os.path.exists(video_path):
        logger.error("❌ [PUBLISHER FAILED] Video file not found: %s", video_path)
        return {"success": False, "error": f"File not found: {video_path}"}

    results = {
        "video_path": video_path,
        "title": title,
        "platforms": {}
    }

    # 1. YouTube Shorts (sync function)
    yt_res = publish_to_youtube(video_path=video_path, title=title, description=description, tags=tags, niche=niche)
    results["platforms"]["youtube"] = yt_res

    # 2. Instagram Reels
    caption_text = f"{title}\n\n{tags}"
    try:
        ig_res = await publish_to_instagram(video_path=video_path, caption=caption_text, niche=niche)
        results["platforms"]["instagram"] = ig_res
    except Exception as e:
        logger.error("❌ Instagram publish error: %s", e)
        results["platforms"]["instagram"] = {"status": "failed", "error": str(e)}

    # 3. TikTok Creator (DISABLED)
    # try:
    #     tt_res = await publish_to_tiktok(video_path=video_path, title=title, tags=tags, niche=niche)
    #     results["platforms"]["tiktok"] = tt_res
    # except Exception as e:
    #     logger.error("❌ TikTok publish error: %s", e)
    #     results["platforms"]["tiktok"] = {"status": "failed", "error": str(e)}
    results["platforms"]["tiktok"] = {"status": "skipped", "message": "TikTok publishing disabled"}

    # 4. Telegram Channel
    try:
        tg_res = await publish_to_telegram(video_path=video_path, title=title, caption=caption_text)
        results["platforms"]["telegram"] = tg_res
    except Exception as e:
        logger.error("❌ Telegram publish error: %s", e)
        results["platforms"]["telegram"] = {"status": "failed", "error": str(e)}

    # Determine overall success
    success_count = sum(1 for p in results["platforms"].values() if p.get("status") == "success")
    results["success"] = success_count > 0
    results["published_count"] = success_count

    logger.info("==================================================================")
    logger.info("🎉 [PHASE 4 COMPLETE] Published across %d/3 platforms (TikTok disabled)!", success_count)
    for p_name, p_data in results["platforms"].items():
        logger.info("   • %s: %s (%s)", p_name.upper(), p_data.get("status"), p_data.get("message") or p_data.get("url") or "ok")
    logger.info("==================================================================")

    return results


def run_phase4_publishing(
    video_path: str,
    title: str,
    description: str = "",
    tags: str = "#viral #shorts #trending",
    niche: Optional[str] = None
) -> Dict[str, Any]:
    """
    Master Orchestration Entry Point for Phase 4 Multi-Platform Publishing.
    Executes sequential 4-platform broadcasting: YouTube -> Instagram -> TikTok -> Telegram.
    Handles running event loops safely.
    """
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = None

    if loop and loop.is_running():
        # Event loop is running — execute async coroutine in existing loop
        import concurrent.futures
        with concurrent.futures.ThreadPoolExecutor() as pool:
            future = pool.submit(
                lambda: asyncio.run(
                    run_phase4_publishing_async(
                        video_path=video_path, title=title, description=description, tags=tags, niche=niche
                    )
                )
            )
            return future.result()
    else:
        return asyncio.run(
            run_phase4_publishing_async(
                video_path=video_path, title=title, description=description, tags=tags, niche=niche
            )
        )


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Phase 4 Multi-Platform Video Publisher")
    parser.add_argument("video", help="Path to .mp4 video file to publish")
    parser.add_argument("--title", "-t", required=True, help="Video title/caption")
    parser.add_argument("--tags", default="#viral #shorts #trending", help="Hashtags")
    args = parser.parse_args()

    res = run_phase4_publishing(video_path=args.video, title=args.title, tags=args.tags)
    print(json.dumps(res, indent=2))

import os
import sys
import asyncio
from dotenv import load_dotenv

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

load_dotenv("Credentials/.env", override=True)
load_dotenv(".env", override=True)

from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup

async def send_test():
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    storage_group_id = os.getenv("TELEGRAM_STORAGE_GROUP_ID")
    chat_id_env = os.getenv("TELEGRAM_CHAT_ID")

    if not token:
        print("❌ TELEGRAM_BOT_TOKEN is missing in .env")
        return

    bot = Bot(token=token)

    # 1. Fetch recent updates to identify user chat ID
    target_chat_ids = set()

    if chat_id_env:
        target_chat_ids.add(int(chat_id_env))

    if storage_group_id:
        target_chat_ids.add(int(storage_group_id))

    try:
        updates = await bot.get_updates()
        for u in updates:
            if u.effective_chat:
                target_chat_ids.add(u.effective_chat.id)
                print(f"📌 Discovered Chat ID from updates: {u.effective_chat.id} ({u.effective_chat.title or u.effective_chat.first_name})")
    except Exception as e:
        print(f"⚠️ get_updates warning: {e}")

    if not target_chat_ids:
        print("❌ No chat IDs found. Please send a message to the bot on Telegram first, then re-run.")
        return

    # Build platform selector keyboard
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("📸 Instagram Creator", callback_data="platform_instagram"),
            InlineKeyboardButton("🔴 YouTube Shorts / Channel", callback_data="platform_youtube"),
        ],
        [
            InlineKeyboardButton("🎵 TikTok Creator", callback_data="platform_tiktok"),
            InlineKeyboardButton("🌐 Direct URL / Raw File", callback_data="platform_direct"),
        ]
    ])

    test_message = (
        "🚀 **Master AI Video Factory Bot is Online & Active!**\n\n"
        "🎯 **Choose your target platform below to begin bulk scraping & editing:**\n"
        "• 📸 **Instagram**: Scrape top reels from creator handle\n"
        "• 🔴 **YouTube**: Scrape Shorts/Videos from channel handle\n"
        "• 🎵 **TikTok**: Scrape top TikTok videos\n"
        "• 🌐 **Direct URL**: Download from any supported site\n\n"
        "👇 **Select your platform or reply with a handle/URL:**"
    )

    for cid in target_chat_ids:
        try:
            await bot.send_message(chat_id=cid, text=test_message, reply_markup=keyboard, parse_mode="Markdown")
            print(f"✅ Successfully sent test message to Telegram Chat ID: {cid}")

            # Save non-group user chat ID to .env if not present
            if cid > 0 and not chat_id_env:
                env_path = ".env"
                if os.path.exists(env_path):
                    with open(env_path, "a", encoding="utf-8") as f:
                        f.write(f"\nTELEGRAM_CHAT_ID={cid}\n")
                    print(f"💾 Saved TELEGRAM_CHAT_ID={cid} to .env")
        except Exception as err:
            print(f"⚠️ Failed to send message to Chat ID {cid}: {err}")

if __name__ == "__main__":
    asyncio.run(send_test())

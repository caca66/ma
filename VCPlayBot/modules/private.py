
import logging
from time import time
from datetime import datetime
from VCPlayBot.config import BOT_USERNAME, BOT_NAME, ASSISTANT_NAME, OWNER_NAME, UPDATES_CHANNEL, SUPPORT_GROUP
from VCPlayBot.helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from VCPlayBot.helpers.decorators import sudo_users_only

logging.basicConfig(level=logging.INFO)


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>- **اهلين  {message.from_user.first_name}** \n
- **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) هو بوت تشغيل اغاني او صوتيات بالمحادثات الصوتيه والمرئيه **

- **سوف تجد طريقة الاستخدام في قسم » الاوامر  !**

- **لروئية الاوامر والشروحات اضغط - /help**
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "➕ اضفني الى مجموعتك ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton(
                        "كيف تستخدمني ؟", callback_data="cbhowtouse")
                ],[
                    InlineKeyboardButton(
                         "الاوامر", callback_data="cbcmds"
                    ),
                    InlineKeyboardButton(
                        "قناة المطور", url=f"https://t.me/NvvvM")
                ],[
                    InlineKeyboardButton(
                        "قناة التحديثات", url=f"https://t.me/{SUPPORT_GROUP}"
                    ),
                    InlineKeyboardButton(
                        "قناة البوت", url=f"https://t.me/{UPDATES_CHANNEL}")
                ],[
                    InlineKeyboardButton(
                        "مطور البوت 🎖", url="https://t.me/C1CIC"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        f"""✅ **bot is running**\n<b>💠 **uptime:**</b> `{uptime}`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✨ Group", url=f"https://t.me/{SUPPORT_GROUP}"
                    ),
                    InlineKeyboardButton(
                        "📣 Channel", url=f"https://t.me/{UPDATES_CHANNEL}"
                    )
                ]
            ]
        )
    )

@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 **آهلا** {message.from_user.mention()}</b>

**اضغط الزر اسفل القائمة لرؤية طريقة الاستخدام والاوامر الخاصه بالبوت !**

⚡ __Powered by {BOT_NAME} A.I""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="طريقة الاستخدام", callback_data="cbguide"
                    )
                ]
            ]
        ),
    )

@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]) & filters.private & ~filters.edited)
async def help_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>- اهلين {message.from_user.mention} من خلال الازرار اسفل القائمة بتقدر تشوف كل الاوامر مع الشرح الخاص فيها ، كل شي سهل يا عزيزي اقراء الاوامر زين وبتفهم كل شي ♥️ !</b>


⚡ __Powered by 𝗔 𝗟 𝗢 𝗡 𝗘 __""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "الاوامر الاساسيه", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "الاوامر المتقدمه", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "اوامر الادمنيه", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "اوامر المطورين", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "اوامر الاونر", callback_data="cbowner"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "", callback_data="cbfun"
                    )
                ]
            ]
        )
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("جاري الحساب...")
    delta_ping = time() - start
    await m_reply.edit_text(
        "سرعة البوت !\n"
        f"⚡️ {delta_ping * 1000:.3f} ms"
    )


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
@sudo_users_only
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 حالة البوت:\n"
        f"• **مدة التشغيل:** `{uptime}`\n"
        f"• **بداية التشفيل:** `{START_TIME_ISO}`"
    )

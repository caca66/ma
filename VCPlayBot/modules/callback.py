# (C) supun-maduraga my best friend for his project on call-music-plus

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from VCPlayBot.helpers.decorators import authorized_users_only
from VCPlayBot.config import BOT_NAME, BOT_USERNAME, OWNER_NAME, SUPPORT_GROUP, UPDATES_CHANNEL, ASSISTANT_NAME
from VCPlayBot.modules.play import cb_admin_check


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>-  **اهلا {query.message.from_user.mention}** \n
-  **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) هو بوت تشغيل اغاني او صوتيات بالمحادثه الصوتيه والمرئيه والقنوات !**

-  **سوف تجد طريقة الاستخدام في خانت » الاوامر اسفل القائمة !**

-  **اذا اردت مساعدة قم بأرسال -  /help**
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
                        "المطور 🎖", url="https://t.me/C1CiC"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex("cbhelp"))
async def cbhelp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>- **اهلا بك في قائمة الاوامر والشروحات !**</b>

**في هذه القائمة ، يمكنك فتح العديد من قوائم الأوامر المتاحة ، وفي كل قائمة أوامر يوجد أيضًا شرح موجز لكل أمر**

⚡ __للاستفسار - [𝐀 𝐋 𝐎 𝐍 𝐄](t.me/C1CIC) -__""",
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
                        "اوامر 𝗢𝘄𝗻𝗲𝗿", callback_data="cbowner"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "", callback_data="cbfun"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "العوده للخلف", callback_data="cbguide"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>قائمة الاوامر الاساسيه </b>

- [ اوامر المجموعة ]

- /play بالرد على الاغنيه للتشغيل
- /ytpplay لتشغيل الاغنيه من اليوتيوب ! 
- /playlist - اظهار الاغاني في الانتظار
- /song + اسم الاغنيه - يقوم بتحميل الاغنيه
- /search + اسم الاغنيه - يقوم بتحميل الاغنيه من اليوتيوب
- /video + اسم الفيديو - يقوم بتحميل الفيديو من اليوتيوب
- /lyrics + اسم الاغنيه - يقوم بظهور كلمات الاغنيه 

- [ اوامر التشغيل في القنوات ]

- /cplay - تشغيل الموسيقى في الدردشة الصوتية
- /cplayer - عرض قائمة الانتظار 
- /cpause - توقف مؤقت 
- /cresume - اكمال بعد التوقف المؤقت 
- /cskip - لتخطي الاغنيه 
- /cend - لايقاف تشغيل الموسيقى 
- /admincache - تحديث قائمة الادمنيه
- /userbotjoin: يدعو الحساب المساعد @{ASSISTANT_NAME} للدردشة الصوتيه

⚡ __للاستفسار - [𝐀 𝐋 𝐎 𝐍 𝐄](t.me/C1CIC)__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "العوده", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbadvanced"))
async def cbadvanced(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>**قائمة الاوامر المتقدمة**</b>

/start (داخل المجموعة) - لرؤية البوت شغال او لا
/clean - تحديث قائمة الملفات
/admincache - تحديث ادمنية البوت
/ping - لعرض سرعة البوت
/uptime - لعرض حالة البوت

⚡ __للاستفسار - [𝐀 𝐋 𝐎 𝐍 𝐄](t.me/C1CIC)__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "العوده", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>**اوامر الادمنيه - المشرفين**</b>

/player - عرض حالة تشغيل الموسيقى
/pause - ايقاف تشغيل الموسيقى مؤقت
/resume - اكمال التوقف المؤقت
/skip - تخطي الاغنيه الحاليه
/end - ايقاف تشغيل الموسيقى
/userbotjoin - دعوة الحساب المساعد للمجموعة
/auth - مستخدم مصرح به لي MusicBot
/deauth - غير مصرح باستخدام بوت الموسيقى
/control - فتح لوحة اعدادات مشغل الموسيقى
/delcmd (on | off) - enable / تعطيل ميزة del Cmd
/musicplayer (on / off) - disable / للتحكم في تشغيل الموسيقى في المجموعة
/b و /tb (حظر / حظر مؤقت) - لحظر البوت بشكل دائم او مؤقت في المجموعة
/ub - إلى مستخدم غير محظور تم حظرك من المجموعة
/m and /tm (mute / temporary mute) - mute permanently or temporarily muted user in group
/um - to unmute user you're muted in group

⚡ __للاستفسار - [𝐀 𝐋 𝐎 𝐍 𝐄](t.me/C1CIC)__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "العوده", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>**اوامر المطورين**</b>

/userbotleaveall - خروج الحساب المساعد من جميع المجموعات
/gcast - اذاعة بأستخدام الحساب المساعد
/stats - اظهار احصائيات البوت
/rmd - مسح جميع التنزيلات
/clean - تحديث الملفات

⚡ __للاستفسار - [𝐀 𝐋 𝐎 𝐍 𝐄](t.me/C1CIC)__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "العوده", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbowner"))
async def cbowner(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>**اوامر الاونر - A L O N E **</b>

/stats - show the bot statistic
/broadcast - send a broadcast message from bot
/block (user id - duration - reason) - block user for using your bot
/unblock (user id - reason) - unblock user you blocked for using your bot
/blocklist - show you the list of user was blocked for using your bot

ملاحظه : **هاذي الاوامر تعمل فقط مع الذي وضعهم الاونر - 
الون مطورين بالبوت فقط لا تعبث بها رجاء 💁🏻‍♂️-

⚡ __للاستفسار - [𝐀 𝐋 𝐎 𝐍 𝐄](t.me/C1CIC)__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "العوده", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbfun"))
async def cbfun(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>/start</b>

⚡ __للاستفسار - [𝐀 𝐋 𝐎 𝐍 𝐄](t.me/C1CIC)__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 BACK", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**كيف تستخدمني ؟**

1.) اضفني الى مجموعتك
2.) اعطني جميع الصلاحيات
3.) اضف @{ASSISTANT_NAME} للمجموعة ثم اكتب  /userbotjoin
4.) تأكد بأن المحادثه الصوتيه شغاله قبل تشغيل الاغنيه 

⚡ __للاستفسار - [𝐀 𝐋 𝐎 𝐍 𝐄](t.me/C1CIC)__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "العودة لقائمة الاوامر", callback_data="cbhelp"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "اغلاق", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()


@Client.on_callback_query(filters.regex("cbback"))
@cb_admin_check
async def cbback(_, query: CallbackQuery):
    await query.edit_message_text(
        "**💡 هنا قائمة التحكم في البوت :**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⏸ تشغيل", callback_data="cbpause"
                    ),
                    InlineKeyboardButton(
                        "▶️ ايقاف مؤقت", callback_data="cbresume"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⏩ تخطي", callback_data="cbskip"
                    ),
                    InlineKeyboardButton(
                        "⏹ ايقاف تشغيل الاغاني", callback_data="cbend"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⛔ anti cmd", callback_data="cbdelcmds"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🛄 group tools", callback_data="cbgtools"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🗑 Close", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbgtools"))
@cb_admin_check
@authorized_users_only
async def cbgtools(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>this is the feature information :</b>

💡 **Feature:** this feature contains functions that can ban, mute, unban, unmute users in your group.

and you can also set a time for the ban and mute penalties for members in your group so that they can be released from the punishment with the specified time.

❔ **usage:**

1️⃣ ban & temporarily ban user from your group:
   » type `/b username/reply to message` ban permanently
   » type `/tb username/reply to message/duration` temporarily ban user
   » type `/ub username/reply to message` to unban user

2️⃣ mute & temporarily mute user in your group:
   » type `/m username/reply to message` mute permanently
   » type `/tm username/reply to message/duration` temporarily mute user
   » type `/um username/reply to message` to unmute user

ملاحظة : يمكن تنفيذ جميع الأوامر التي يمتلكها هذا البوت بواسطة مالك البوت - الون دون أي استثناءات.

⚡ __للاستفسار - [𝐀 𝐋 𝐎 𝐍 𝐄](t.me/C1CIC)__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "العودة للخلف", callback_data="cbback"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbdelcmds"))
@cb_admin_check
@authorized_users_only
async def cbdelcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>this is the feature information :</b>
        
**💡 Feature:** delete every commands sent by users to avoid spam in groups !

❔ usage:**

 1️⃣ to turn on feature:
     » type `/delcmd on`
    
 2️⃣ to turn off feature:
     » type `/delcmd off`
      
⚡ __للاستفسار - [𝐀 𝐋 𝐎 𝐍 𝐄](t.me/C1CIC)__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "العوده للخلف", callback_data="cbback"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbhelps(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>- **اهلا بك في قائمة الاوامر والشروحات !**</b>

**في هذه القائمة ، يمكنك فتح العديد من قوائم الأوامر المتاحة ، وفي كل قائمة أوامر يوجد أيضًا شرح موجز لكل أمر**


⚡ __للاستفسار - [𝐀 𝐋 𝐎 𝐍 𝐄](t.me/C1CIC)__""",
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
                        "اوامر 𝗢𝘄𝗻𝗲𝗿", callback_data="cbowner"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "", callback_data="cbfun"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "العوده للقائمة الرئيسيه", callback_data="cbstart"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""كيف تستخدمني ؟:

1.) اضفني الى مجموعتك
2.) اعطني جميع الصلاحيات
3.) اضف @{ASSISTANT_NAME} للمجموعة ثم اكتب  /userbotjoin
4.) تأكد بأن المحادثه الصوتيه شغاله قبل تشغيل الاغنيه 

⚡ __للاستفسار - [𝐀 𝐋 𝐎 𝐍 𝐄](t.me/C1CIC)__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "العوده للقائمة الرئيسيه", callback_data="cbstart"
                    )
                ]
            ]
        )
    )

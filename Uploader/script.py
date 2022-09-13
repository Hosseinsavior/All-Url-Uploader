# MIT License

# Copyright (c) 2022 Hash Minner

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class Translation(object):

    START_TEXT = """
👋ʜɪ {} 

ɪ ᴀᴍ ᴘᴏᴡᴇʀꜰᴜʟ ᴜʀʟ ᴜᴘʟᴏᴀᴅᴇʀ ʙᴏᴛ

⏩𝘼 𝙨𝙞𝙢𝙥𝙡𝙚 𝙩𝙚𝙡𝙚𝙜𝙧𝙖𝙢 𝘽𝙤𝙩, 𝙐𝙥𝙡𝙤𝙖𝙙 𝙈𝙚𝙙𝙞𝙖 𝙁𝙞𝙡𝙚| 𝙫𝙞𝙙𝙚𝙤 𝙏𝙤 𝙩𝙚𝙡𝙚𝙜𝙧𝙖𝙢 𝙪𝙨𝙞𝙣𝙜 𝙩𝙝𝙚 𝙙𝙞𝙧𝙚𝙘𝙩 𝙙𝙤𝙬𝙣𝙡𝙤𝙖𝙙 𝙡𝙞𝙣𝙠. (𝙮𝙤𝙪𝙩𝙪𝙗𝙚, 𝙈𝙚𝙙𝙞𝙖𝙛𝙞𝙧𝙚, 𝙜𝙤𝙤𝙜𝙡𝙚 𝙙𝙧𝙞𝙫𝙚, 𝙢𝙚𝙜𝙖 𝙙𝙧𝙞𝙫𝙚, 𝙚𝙩𝙘)
𝙔𝙤𝙪𝙩𝙪𝙗𝙚, 𝙂𝙤𝙤𝙜𝙡𝙚𝘿𝙧𝙞𝙫𝙚, 𝘼𝙥𝙥𝙡𝙚 𝙈𝙪𝙨𝙞𝙘, 𝙎𝙥𝙤𝙩𝙞𝙛𝙮, 𝙍𝙚𝙨𝙨𝙤, & 𝘿𝙞𝙧𝙚𝙘𝙩 𝙇𝙞𝙣𝙠𝙨 𝙨𝙪𝙥𝙥𝙤𝙧𝙩.
𝘽𝙤𝙩 𝘾𝙖𝙣 𝙪𝙥𝙡𝙤𝙖𝙙 𝙙𝙤𝙘𝙪𝙢𝙚𝙣𝙩, 𝙫𝙞𝙙𝙚𝙤 & 𝙖𝙪𝙙𝙞𝙤 𝙩𝙮𝙥𝙚𝙨.
𝘿𝙚𝙥𝙡𝙤y | 𝙡𝙤𝙘𝙖𝙡𝙡𝙮 | 𝙑𝙋𝙎.
𝘾𝙪𝙨𝙩𝙤𝙢 𝙩𝙝𝙪𝙢𝙗𝙣𝙖𝙞𝙡 𝙨𝙪𝙥𝙥𝙤𝙧𝙩.
/𝙩𝙝𝙪𝙢𝙗 - 𝙫𝙞𝙚𝙬 𝙮𝙤𝙪𝙧 𝙘𝙪𝙨𝙩𝙤𝙢 𝙩𝙝𝙪𝙢𝙗𝙪𝙣𝙡𝙞
/𝙙𝙚𝙡𝙩𝙝𝙪𝙢𝙗 - 𝙙𝙚𝙡𝙚𝙩𝙚 𝙮𝙤𝙪𝙧 𝙘𝙪𝙨𝙩𝙤𝙢 𝙩𝙝𝙪𝙢𝙗𝙪𝙣𝙡𝙞
 
"""

    HELP_TEXT = """

𝑺𝒆𝒏𝒅 𝒎𝒆 𝒕𝒉𝒆 𝑮𝒐𝒐𝒈𝒍𝒆 𝑫𝒓𝒊𝒗𝒆 | 𝒚𝒕𝒅𝒍 | 𝒅𝒊𝒓𝒆𝒄𝒕 𝒍𝒊𝒏𝒌𝒔.

 𝑺𝒆𝒍𝒆𝒄𝒕 𝒕𝒉𝒆 𝒅𝒆𝒔𝒊𝒓𝒆𝒅 𝒐𝒑𝒕𝒊𝒐𝒏.

𝑻𝒉𝒆𝒏 𝒃𝒆 𝒓𝒆𝒍𝒂𝒙𝒆𝒅 𝒚𝒐𝒖𝒓 𝒇𝒊𝒍𝒆 𝒘𝒊𝒍𝒍 𝒃𝒆 𝒖𝒑𝒍𝒐𝒂𝒅𝒆𝒅 𝒔𝒐𝒐𝒏..
 
"""

# give credit to developer

    ABOUT_TEXT = """
<b>♻️ My Name</b> : 𝑃𝑜𝑤𝑒𝑟𝑓𝑢𝑙 𝑈𝑅𝐿 𝐷𝑜𝑤𝑛𝑙𝑜𝑑𝑒𝑟

<b>🌀 Channel</b> : <a href="https://t.me/SaviorisGod">Savior</a>


<b>👲 Developer :</b> <a href="https://t.me/Savior_128">sᎪᏉᎥᎾᏒ_128</a>

"""

    PROGRESS = """
🔰 Speed : {3}/s\n\n
🌀 Done : {1}\n\n
🎥 Tᴏᴛᴀʟ sɪᴢᴇ  : {2}\n\n
⏳ Tɪᴍᴇ ʟᴇғᴛ : {4}\n\n
"""
    ID_TEXT = """
🆔 Your Telegram ID 𝐢𝐬 :- <code>{}</code>
"""

    INFO_TEXT = """

 🤹 First Name : <b>{}</b>

 🚴‍♂️ Second Name : <b>{}</b>

 🧑🏻‍🎓 Username : <b>@{}</b>

 🆔 Telegram Id : <code>{}</code>

 📇 Profile Link : <b>{}</b>

 📡 Dc : <b>{}</b>

 📑 Language : <b>{}</b>

 👲 Status : <b>{}</b>
"""

    START_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('❓ Help', callback_data='help'),
            InlineKeyboardButton('🦊 About', callback_data='about')
        ], [
            InlineKeyboardButton('📛 Close', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('🏠 Home', callback_data='home'),
            InlineKeyboardButton('🦊 About', callback_data='about')
        ], [
            InlineKeyboardButton('📛 Close', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('🏠 Home', callback_data='home'),
            InlineKeyboardButton('❓ Help', callback_data='help')
        ], [
            InlineKeyboardButton('📛 Close', callback_data='close')
        ]]
    )
    BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('📛 Close', callback_data='close')
        ]]
    )
    FORMAT_SELECTION = "Now Select the desired formats"
    SET_CUSTOM_USERNAME_PASSWORD = """"""
    DOWNLOAD_START = "𝚃𝚛𝚢𝚒𝚗𝚐 𝚝𝚘 𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍 𝚙𝚕𝚎𝚊𝚜𝚎 𝚠𝚊𝚒𝚝...⌛\n\n <i>{} </i>"
    UPLOAD_START = "<i>{} </i>\n\n📤 Uploading Please Wait "
    RCHD_TG_API_LIMIT = "𝘿𝙤𝙬𝙣𝙡𝙤𝙖𝙙𝙚𝙙 𝙞𝙣 {} 𝙨𝙚𝙘𝙤𝙣𝙙𝙨.\𝙣𝘿𝙚𝙩𝙚𝙘𝙩𝙚𝙙 𝙁𝙞𝙡𝙚 𝙎𝙞𝙯𝙚: {}\𝙣𝙎𝙤𝙧𝙧𝙮. 𝘽𝙪𝙩, 𝙄 𝙘𝙖𝙣𝙣𝙤𝙩 𝙪𝙥𝙡𝙤𝙖𝙙 𝙛𝙞𝙡𝙚𝙨 𝙜𝙧𝙚𝙖𝙩𝙚𝙧 𝙩𝙝𝙖𝙣 𝟐𝙂𝘽 𝙙𝙪𝙚 𝙩𝙤 𝙏𝙚𝙡𝙚𝙜𝙧𝙖𝙢 𝘼𝙋𝙄 𝙡𝙞𝙢𝙞𝙩𝙖𝙩𝙞𝙤𝙣𝙨."
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Dᴏᴡɴʟᴏᴀᴅᴇᴅ ɪɴ {} sᴇᴄᴏɴᴅs.\n\nTʜᴀɴᴋs Fᴏʀ Usɪɴɢ Mᴇ\n\nUᴘʟᴏᴀᴅᴇᴅ ɪɴ {} sᴇᴄᴏɴᴅs"
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media cleared succesfully."
    CUSTOM_CAPTION_UL_FILE = " "
    NO_VOID_FORMAT_FOUND = "ERROR... <code>{}</code>"
    SLOW_URL_DECED = "𝔾𝕠𝕤𝕙 𝕥𝕙𝕒𝕥 𝕤𝕖𝕖𝕞𝕤 𝕥𝕠 𝕓𝕖 𝕒 𝕧𝕖𝕣𝕪 𝕤𝕝𝕠𝕨 𝕌ℝ𝕃. 𝕊𝕚𝕟𝕔𝕖 𝕪𝕠𝕦 𝕨𝕖𝕣𝕖 𝕤𝕔𝕣𝕖𝕨𝕚𝕟𝕘 𝕞𝕪 𝕙𝕠𝕞𝕖, 𝕀 𝕒𝕞 𝕚𝕟 𝕟𝕠 𝕞𝕠𝕠𝕕 𝕥𝕠 𝕕𝕠𝕨𝕟𝕝𝕠𝕒𝕕 𝕥𝕙𝕚𝕤 𝕗𝕚𝕝𝕖. 𝕄𝕖𝕒𝕟𝕨𝕙𝕚𝕝𝕖, 𝕨𝕙𝕪 𝕕𝕠𝕟'𝕥 𝕪𝕠𝕦 𝕥𝕣𝕪 𝕥𝕙𝕚𝕤:==> 𝕙𝕥𝕥𝕡𝕤://𝕤𝕙𝕣𝕥𝕫.𝕞𝕖/ℙ𝕥𝕤𝕍𝕟𝕗𝟞 𝕒𝕟𝕕 𝕘𝕖𝕥 𝕞𝕖 𝕒 𝕗𝕒𝕤𝕥 𝕌ℝ𝕃 𝕤𝕠 𝕥𝕙𝕒𝕥 𝕀 𝕔𝕒𝕟 𝕦𝕡𝕝𝕠𝕒𝕕 𝕥𝕠 𝕋𝕖𝕝𝕖𝕘𝕣𝕒𝕞, 𝕨𝕚𝕥𝕙𝕠𝕦𝕥 𝕞𝕖 𝕤𝕝𝕠𝕨𝕚𝕟𝕘 𝕕𝕠𝕨𝕟 𝕗𝕠𝕣 𝕠𝕥𝕙𝕖𝕣 𝕦𝕤𝕖𝕣𝕤."

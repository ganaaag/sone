from pyrogram import Client as bot, filters
from main import LOGGER
import master.helper as helper
import shutil
import os
from master import process
import msg

@bot.on_message(filters.command("drm"))
async def drm_download(bot, m):
    files_cleared = False
    temp_dir = os.path.join(os.getcwd(), "temp")
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
        files_cleared = True 
    if files_cleared:
        LOGGER.info("✅**Files with specified extensions and temp directory cleared successfully!**✅")
    else:
        LOGGER.info("No files with specified extensions were found, and temp directory was not present.")
    editable = await m.reply_text('<b><i>Hii, I am non-drm Downloader Bot</b></i>\n<b><i><blockquote>Send Me Your text file which enclude Name with url... E.g: Name: Link</b></i></blockquote>')
    input = await bot.listen(chat_id=m.chat.id)
    links , file_name = await helper.process_text_file_or_input(bot, input, m)
    if not links:
        await editable.delete()
        await bot.send_message(m.chat.id, msg.planMessage)
        return
    await editable.edit(f"Total links🔗 found are __{len(links)}__\n\nSend From where you want to download. initial is __1__")
    input0 = await bot.listen(chat_id=m.chat.id)
    raw_text = input0.text
    await input0.delete()
    await editable.edit("__Enter Batch Name or send /d for filename.__")
    input1 = await bot.listen(chat_id=m.chat.id)
    b_name = input1.text if input1.text != '/d' else file_name
    await input1.delete()

    quality_to_resolution = {
        240: "426x240",
        360: "640x360",
        400: "400x224",
        480: "854x480",
        540: "960x540",
        576: "1024x576",
        720: "1280x720",
        1080: "1920x1080"
    }
    await editable.edit("__Enter resolution or Video Quality (240, 360, 400, 480, 540, 576, 720, 1080)__")
    input2 = await bot.listen(chat_id=m.chat.id)
    try:
        quality = int(input2.text)
        if quality in quality_to_resolution:
            selected_resolution = quality_to_resolution[quality]
        else:
            await editable.edit("__Invalid input! Please enter a valid resolution (240, 360, 480, 540, 576, 720, 1080)__")
    except ValueError:
        await editable.edit("__Please enter a numeric value for the resolution!__")
        return
    await input2.delete()
    await editable.edit("<b><i>Enter the credit name for the caption. If you want both a permanent credit in the caption and the file name, separate them with a comma (,). or you want default then send /d</i>\n\n<blockquote>Example for caption only: `Admin`\nExample for both caption and file name: `Admin,Admin`</blockquote></b>")
    input3 = await bot.listen(chat_id=m.chat.id)
    Credit = input3.text.strip()
    FileNameCredit = ''
    if "," in Credit:
        credit, FileNameCredit = Credit.split(",")
    else:
        credit = input3.text if input3.text != '/d' else "Admin"
    await input3.delete()

    await editable.edit("<b><i>Send the Thumb URL <u>(e.g., https://telegra.ph/file/0eca3245df8a4SE0c7e68d4.jpg)</u> for default thumbnail /d </b></i>\n<blockquote><b><i>If You want to use Watermark Overlay as thumbnail then Just Send Your Name in Simple Font.. (Eg:- Admin)</blockquote></b></i>", disable_web_page_preview=True)
    input6 = await bot.listen(chat_id=m.chat.id)
    thumbs = input6.text.strip()
    watermark = None
    if "," in thumbs:
        thumb, watermark = thumbs.split(",")
    else:
        thumb = thumbs
    await input6.delete()

    await editable.edit("<b><i>⚠️Provide the Channel ID or send /d</b></i>\n\n<blockquote><b><i>🔹 Make me an admin to upload.\n🔸Send /id in your channel to get the Channel ID.\n\nExample: Channel ID = -1002149983828 or /d for Personally</i></b></blockquote>"
    )
    input7 = await bot.listen(chat_id=m.chat.id)
    channel_id = input7.text if "/d" not in input7.text else m.chat.id
    await input7.delete()
    if channel_id == m.chat.id:
        await editable.delete()
    else:
        await editable.edit(f"<blockquote><b><i>🎯**Target Batch - {b_name}</blockquote></b></i>\n\n<b><i>🔄 Your Task is under processing, please check your Set Channel📱. Once your task is complete, I will inform you 📩</b></i>")
    try:
        await bot.send_message(chat_id=channel_id, text=f'<blockquote><b><i>🎯Target Batch - {b_name}</blockquote></b></i>')
    except Exception as e:
        await m.reply_text(f"<b><i>Fail Reason »</b></i> \n<blockquote><b><i>{e}</i></b></blockquote>")
        return
    await process.process(bot, m, links, raw_text, channel_id, b_name, credit, FileNameCredit, selected_resolution, thumb, watermark, editable, quality)


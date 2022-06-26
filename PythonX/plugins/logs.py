
import asyncio
from PythonX import MK1, MK2, MK3, MK4, MK5, MK6, MK7, MK8, MK9, MK10, OWNER_ID, HEROKU_API_KEY, HEROKU_APP_NAME
from .. import CMD_HNDLR as hl
from telethon import events
from datetime import datetime
import heroku3

Heroku = heroku3.from_key(HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
 
 
@MK1.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@MK2.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@MK3.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@MK4.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@MK5.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@MK6.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@MK7.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@MK8.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@MK9.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@MK10.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
async def logs(legend):
    if legend.sender_id == OWNER_ID:
        if (HEROKU_APP_NAME is None) or (HEROKU_API_KEY is None):
            return await legend.reply(
                legend.chat_id,
                "First Set These Vars In Heroku :  `HEROKU_API_KEY` And `HEROKU_APP_NAME`.",
            )
        try:
            Heroku = heroku3.from_key(HEROKU_API_KEY)
            app = Heroku.app(HEROKU_APP_NAME)
        except BaseException:
            return await legend.reply(
                "Make Sure Your Heroku API Key & App Name Are Configured Correctly In Heroku."
            )
        logs = app.get_log()
        start = datetime.now()
        fetch = await legend.reply("__Fetching Logs...__")
        end = datetime.now()
        ms = (end-start).seconds
        await asyncio.sleep(1)
        await fetch.delete()
        logfile = open("BotSpamLogs.txt", "w")
        logfile.write("⚡ PythonX ⚡ [ BotSpam Logs ]\n\n" + logs)
        logfile.close()
        await MK1.send_file(legend.chat_id, "BotSpamLogs.txt", caption=f"⚡ 𝐏𝐲𝐭𝐡𝐨𝐧𝐗 𝐋𝐨𝐠𝐬 ⚡\n**Time Taken :** `{ms} Seconds`")
    else:
        await legend.reply("Sorry, Only Owner Can Access This Command.")

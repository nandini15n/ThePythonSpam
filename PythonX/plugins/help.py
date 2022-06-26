from PythonX import MK1, MK2, MK3, MK4, MK5, MK6, MK7, MK8, MK9, MK10, SUDO_USERS
from telethon import events, Button
from PythonX import CMD_HNDLR as hl
    
HELP_PIC = "https://te.legra.ph/file/57ef20b6463f2596e9b21.jpg"

PythonHelp = "★ 𝙏𝙝𝙚𝙋𝙮𝙩𝙝𝙤𝙣𝙎𝙥𝙖𝙢 𝙃𝙚𝙡𝙥 𝙈𝙚𝙣𝙪 ★\n𝐂𝐥𝐢𝐜𝐤 𝐎𝐧 𝐁𝐞𝐥𝐨𝐰 𝐁𝐮𝐭𝐭𝐨𝐧𝐬 𝐅𝐨𝐫 𝐇𝐞𝐥𝐩\n\n\n@ALLENite_X"


@MK1.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@MK2.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@MK3.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@MK4.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@MK5.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@MK6.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@MK7.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@MK8.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@MK9.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@MK10.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):
    if event.sender_id in SUDO_USERS:
       await event.client.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=PythonHelp,
                                  buttons=[
           [
            Button.inline("🔥 Spam 🔥", data="spam"),
            Button.inline("😈 Raid 😈", data="raid"),
           ],
           [
            Button.inline("⚡ Extra ⚡", data="extra"),
           ],
           [    
            Button.url("✨ ᴄʜᴀɴɴᴇʟ ✨", "https://t.me/MKxHACKER")
           ],
           [
           Button.url("✨ sᴜᴘᴘᴏʀᴛ ✨", "https://t.me/HACKERxSPAM")
           ],
           ],
           )              

  
  
extra_msg = f"""
**Help Extra Cmds**

**UserBot :** Userbot Cmds
Command :
1) {hl}ping 
2) {hl}alive
3) {hl}restart
4) {hl}addsudo <reply to user> || Owner Cmd ||
5) {hl}logs || Owner Cmd ||

**Echo :** To Active Echo On Any User
Command :
1) {hl}addecho <reply to user>
2) {hl}rmecho <reply to user>

**Leave :** To Leave Group/Channel
Command :
1) {hl}leave <group/chat id>
2) {hl}leave : Type in the Group bot will auto leave that group

**PackSpam :** Sticker Pack Spam
1) {hl}packspam <reply to any sticker>

**© @ALLENite_X**
"""

                 
raid_msg = f"""
**Help Raid Cmds**


**Raid :** Activates Raid on Any individual User For Given Range.
Command :
1) {hl}raid <count> <username>
2) {hl}raid <count> <reply to user>

**DelayRaid :** Activates Raid on Any individual User For Given Range.
Command :
1) {hl}delayraid <delay> <count> <Username of User>
2) {hl}delayraid <delay> <count> <reply to a User>

**ReplyRaid :** Activates Reply Raid on The User!!
Command :
1) {hl}replyraid <replying to user>
2) {hl}dreplyraid <username>

**DReplyRaid :** Deactivates Reply Raid on The User!!
Command :
1) {hl}dreplyraid <replying to user>
2) {hl}dreplyraid <username>


**© @ALLENite_X**
"""

spam_msg = f"""
**Help Spam Cmds**

**Spam :** Spams a Message.
Command :
1) {hl}spam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
2) {hl}spam <count> <replying any message>

**DelaySpam :** Delay Spam a Text For Given Counter After Given Time.
Command :
1) {hl}delayspam <delay> <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
2) {hl}delayspam <delay> <count> <replying any message>

**PormSpam :** Pormography Spam.
Command :
1) {hl}pornspam <count>

**Hang :** Spams Hanging Message For Given Counter.
Command :
1) {hl}hang <counter> (you can reply any message if you want bot to reply that message and do spamming)

** © @ALLENite_X**
"""                     
           
           
@MK1.on(events.CallbackQuery(pattern=r"help_back"))
@MK2.on(events.CallbackQuery(pattern=r"help_back"))
@MK3.on(events.CallbackQuery(pattern=r"help_back"))
@MK4.on(events.CallbackQuery(pattern=r"help_back"))
@MK5.on(events.CallbackQuery(pattern=r"help_back"))
@MK6.on(events.CallbackQuery(pattern=r"help_back"))
@MK7.on(events.CallbackQuery(pattern=r"help_back"))
@MK8.on(events.CallbackQuery(pattern=r"help_back"))
@MK9.on(events.CallbackQuery(pattern=r"help_back"))
@MK10.on(events.CallbackQuery(pattern=r"help_back"))
async def helpback(event):
   if event.query.user_id in SUDO_USERS:    
      await event.edit(
            PythonHelp,
            buttons=[
           [
            Button.inline("🔥 Spam 🔥", data="spam"),
            Button.inline("😈 Raid 😈", data="raid"),
           ],
           [
            Button.inline("⚡ Extra ⚡", data="extra"),
           ],
           [    
            Button.url("✨ ᴄʜᴀɴɴᴇʟ ✨", "https://t.me/MKxHACKER")
           ],
           [
           Button.url("✨ sᴜᴘᴘᴏʀᴛ ✨", "https://t.me/HACKERxSPAM")
           ],
           ],
        )           
   else:
        Alert = (
                "Make Your Own PythonX Bots !! @ALLENite_X"
            )
        await event.answer(Alert, cache_time=0, alert=True)
      
           
                      
@MK1.on(events.CallbackQuery(pattern=r"spam"))
@MK2.on(events.CallbackQuery(pattern=r"spam"))
@MK3.on(events.CallbackQuery(pattern=r"spam"))
@MK4.on(events.CallbackQuery(pattern=r"spam"))
@MK5.on(events.CallbackQuery(pattern=r"spam"))
@MK6.on(events.CallbackQuery(pattern=r"spam"))
@MK7.on(events.CallbackQuery(pattern=r"spam"))
@MK8.on(events.CallbackQuery(pattern=r"spam"))
@MK9.on(events.CallbackQuery(pattern=r"spam"))
@MK10.on(events.CallbackQuery(pattern=r"spam"))
async def help_spam(event):
   if event.query.user_id in SUDO_USERS:    
       await event.edit(
            spam_msg,
            buttons=[
                [
            Button.inline("< Back", data="help_back"),
            ],
            ],
            ) 
   else:
        Alert = (
                "Make Your Own PythonX Bots !! @ALLENite_X"
            )
        await event.answer(Alert, cache_time=0, alert=True)
                 
                                                       
@MK1.on(events.CallbackQuery(pattern=r"raid"))
@MK2.on(events.CallbackQuery(pattern=r"raid"))
@MK3.on(events.CallbackQuery(pattern=r"raid"))
@MK4.on(events.CallbackQuery(pattern=r"raid"))
@MK5.on(events.CallbackQuery(pattern=r"raid"))
@MK6.on(events.CallbackQuery(pattern=r"raid"))
@MK7.on(events.CallbackQuery(pattern=r"raid"))
@MK8.on(events.CallbackQuery(pattern=r"raid"))
@MK9.on(events.CallbackQuery(pattern=r"raid"))
@MK10.on(events.CallbackQuery(pattern=r"raid"))
async def help_raid(event):
     if event.query.user_id in SUDO_USERS:
        await event.edit(
            raid_msg,
            buttons=[
            [
            Button.inline("< Back", data="help_back"),
            ],
            ],
            )  
     else:
        Alert = (
                "Make Your Own PythonX Bots !! @ALLENite_X"
            )
        await event.answer(Alert, cache_time=0, alert=True)
       


@MK1.on(events.CallbackQuery(pattern=r"extra"))
@MK2.on(events.CallbackQuery(pattern=r"extra"))
@MK3.on(events.CallbackQuery(pattern=r"extra"))
@MK4.on(events.CallbackQuery(pattern=r"extra"))
@MK5.on(events.CallbackQuery(pattern=r"extra"))
@MK6.on(events.CallbackQuery(pattern=r"extra"))
@MK7.on(events.CallbackQuery(pattern=r"extra"))
@MK8.on(events.CallbackQuery(pattern=r"extra"))
@MK9.on(events.CallbackQuery(pattern=r"extra"))
@MK10.on(events.CallbackQuery(pattern=r"extra"))
async def help_extra(event):
   if event.query.user_id in SUDO_USERS:
        await event.edit(
            extra_msg,
            buttons=[
            [
            Button.inline("< Back", data="help_back"),                        
            ],
            ],
            )
   else:
        Alert = (
                "Make Your Own PythonX Bots !! @ALLENite_X"
            )
        await event.answer(Alert, cache_time=0, alert=True)

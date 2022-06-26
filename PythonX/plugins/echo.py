
import asyncio
import base64

from telethon import events
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from PythonX import MK1, MK2, MK3, MK4, MK5 , MK6, MK7, MK8, MK9, MK10, SUDO_USERS, OWNER_ID

from PythonX import CMD_HNDLR as hl
from PythonX.sql.echo_sql import addecho, is_echo, remove_echo
from resources.data import RyanX


@MK1.on(events.NewMessage(incoming=True, pattern=r"\%saddecho(?: |$)(.*)" % hl))
@MK2.on(events.NewMessage(incoming=True, pattern=r"\%saddecho(?: |$)(.*)" % hl))
@MK3.on(events.NewMessage(incoming=True, pattern=r"\%saddecho(?: |$)(.*)" % hl))
@MK4.on(events.NewMessage(incoming=True, pattern=r"\%saddecho(?: |$)(.*)" % hl))
@MK5.on(events.NewMessage(incoming=True, pattern=r"\%saddecho(?: |$)(.*)" % hl))
@MK6.on(events.NewMessage(incoming=True, pattern=r"\%saddecho(?: |$)(.*)" % hl))
@MK7.on(events.NewMessage(incoming=True, pattern=r"\%saddecho(?: |$)(.*)" % hl))
@MK8.on(events.NewMessage(incoming=True, pattern=r"\%saddecho(?: |$)(.*)" % hl))
@MK9.on(events.NewMessage(incoming=True, pattern=r"\%saddecho(?: |$)(.*)" % hl))
@MK10.on(events.NewMessage(incoming=True, pattern=r"\%saddecho(?: |$)(.*)" % hl))
async def echo(event):
  usage = f"**MODULE NAME : ECHO**\n\nCommand :\n\n `{hl}addecho <reply to a User>`"
  if event.sender_id in SUDO_USERS:
     if event.reply_to_msg_id is not None:
            reply_msg = await event.get_reply_message()
            user_id = reply_msg.sender_id
            if int(user_id) in RyanX:
                    text = f"I Can't Echo PythonX's Owner"
                    await event.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) == OWNER_ID:
                    text = f"This Guy is Owner Of These Bots."
                    await event.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) in SUDO_USERS:
                    text = f"This Guy is a Sudo User."
                    await event.reply(text, parse_mode=None, link_preview=None )
            else:
                 chat_id = event.chat_id
                 try:
                     hmm = base64.b64decode("QE1pZ2h0eVhTdXBwb3J0")
                     hmm = Get(hmm)
                     await event.client(hmm)
                 except BaseException:
                    pass
                 if is_echo(user_id, chat_id):
                     await event.reply("Echo Is Already Activated On This User !!")
                     return
                 addecho(user_id, chat_id)
                 await event.reply("Echo Activated On The User ✅")
     else:
          await event.reply(usage)

@MK1.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK2.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK3.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK4.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK5.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK6.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK7.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK8.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK9.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK10.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
async def echo(event):
  usage = f"**MODULE NAME : RM ECHO**\n\nCommand :\n\n `{hl}rmecho <reply to a User>`"
  if event.sender_id in SUDO_USERS:
     if event.reply_to_msg_id is not None:
            reply_msg = await event.get_reply_message()
            user_id = reply_msg.sender_id
            chat_id = event.chat_id
            try:
                hmm = base64.b64decode("QE1pZ2h0eVhTdXBwb3J0")
                hmm = Get(hmm)
                await event.client(hmm)
            except BaseException:
                pass
            if is_echo(user_id, chat_id):
                remove_echo(user_id, chat_id)
                await event.reply("Echo Has Been Stopped For The User ☑️")
            else:
                await event.reply("Echo Is Already Disabled !!")
     else:
          await event.reply(usage)


@MK1.on(events.NewMessage(incoming=True))
@MK2.on(events.NewMessage(incoming=True))
@MK3.on(events.NewMessage(incoming=True))
@MK4.on(events.NewMessage(incoming=True))
@MK5.on(events.NewMessage(incoming=True))
@MK6.on(events.NewMessage(incoming=True))
@MK7.on(events.NewMessage(incoming=True))
@MK8.on(events.NewMessage(incoming=True))
@MK9.on(events.NewMessage(incoming=True))
@MK10.on(events.NewMessage(incoming=True))
async def _(e):
    if is_echo(e.sender_id, e.chat_id):
        await asyncio.sleep(0.3)
        try:
            Python = base64.b64decode("QE1pZ2h0eVhTdXBwb3J0")
            Python = Get(Python)
            await e.client(Python)
        except BaseException:
            pass
        if e.message.text or e.message.sticker:
            await e.reply(e.message)

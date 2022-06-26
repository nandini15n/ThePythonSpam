
import asyncio
import random
from telethon import events
from PythonX import MK1, MK2, MK3, MK4, MK5 , MK6, MK7, MK8, MK9, MK10, SUDO_USERS, OWNER_ID
from resources.data import RAID, REPLYRAID, RyanX, MRAID, SRAID, CRAID
from PythonX import CMD_HNDLR as hl


que = {}


@MK1.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK2.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK3.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK4.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK5.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK6.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK7.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK8.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK9.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK10.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗮𝗶𝗱\n\nCommand:\n\n.raid <count> <Username of User>\n\n.raid <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        mkraid = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        await e.get_reply_message()
        if len(mkraid) == 2:
            message = str(mkraid[1])
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(mkraid[0])
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.1)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            c = b.first_name
            counter = int(mkraid[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.1)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )



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
async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.2)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(REPLYRAID)),
            reply_to=event.message.id,
        )


@MK1.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@MK2.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@MK3.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@MK4.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@MK5.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@MK6.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@MK7.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@MK8.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@MK9.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@MK10.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
async def _(e):
    global que
    usage = f"**MODULE NAME : REPLY RAID**\n\nCommand:\n\n{hl}replyraid <Username of User>\n\n{hl}replyraid <reply to a User>."
    if e.sender_id in SUDO_USERS:
        mkrr = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        mkr = await e.get_reply_message()
        if len(e.text) > 11:
            message = str(mkrr[0])
            a = await e.client.get_entity(message)
            user_idd = a.id
            user_id = int(user_idd)
            if int(user_id) in RyanX:
                text = f"Sorry, I Can't Raid On PythonX's Owner."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) == OWNER_ID:
                text = f"This Guy is Owner Of These Bots."            
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) in SUDO_USERS:
                text = f"This Guy is a Sudo User."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                que[user_id] = []
                gey = que.get(user_id)
                phucker = [user_id]
                gey.append(phucker)
                text = f"Activated ReplyRaid !! ✅"
                await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            umser = await e.client.get_entity(a.sender_id)
            user_idd = umser.id
            user_id = int(user_idd)
            if int(user_id) in RyanX:
                text = f"Sorry, I Can't Raid  On PythonX's Owner."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) == OWNER_ID:
                text = f"This Guy is Owner Of These Bots."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) in SUDO_USERS:
                text = f"This Guy is a Sudo User."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                que[user_id] = []
                gey = que.get(user_id)
                phucker = [user_id]
                gey.append(phucker)
                text = f"Activated ReplyRaid !! ✅"
                await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage)


@MK1.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@MK2.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@MK3.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@MK4.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@MK5.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@MK6.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@MK7.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@MK8.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@MK9.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@MK10.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
async def _(e):
    usage = f"**MODULE NAME : DREPLYRAID**\n\nCommand:\n\n{hl}dreplyraid <Username of User>\n\n{hl}dreplyraid <reply to a User>"
    global que    
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        Migoel = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 12:
            message = str(Migoel[0])
            a = await e.client.get_entity(message)
            g = a.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "Reply Raid De-Activated !! ✅"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "Reply Raid De-Activated !! ✅"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage)



@MK1.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK2.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK3.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK4.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK5.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK6.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK7.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK8.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK9.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK10.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗠𝗥𝗮𝗶𝗱\n\nCommand:\n\n.mraid <count> <Username of User>\n\n.mraid <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        mkmr = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        await e.get_reply_message()
        if len(mkmr) == 2:
            message = str(mkmr[1])
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(mkmr[0])
            for _ in range(counter):
                reply = random.choice(MRAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            c = b.first_name
            counter = int(mkmr[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(MRAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.1)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )




@MK1.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK2.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK3.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK4.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK5.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK6.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK7.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK8.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK9.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK10.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗦𝗥𝗮𝗶𝗱\n\nCommand:\n\n.sraid <count> <Username of User>\n\n.sraid <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        MKsr = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        await e.get_reply_message()
        if len(MKsr) == 2:
            message = str(MKsr[1])
            print(message)
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(MKsr[0])
            for _ in range(counter):
                reply = random.choice(SRAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            c = b.first_name
            counter = int(MKsr[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(SRAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.1)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )




@MK1.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK2.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK3.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK4.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK5.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK6.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK7.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK8.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK9.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK10.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = C𝗥𝗮𝗶𝗱\n\nCommand:\n\n.craid <count> <Username of User>\n\n.craid <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        MKsr = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        await e.get_reply_message()
        if len(MKsr) == 2:
            message = str(MKsr[1])
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(MKsr[0])
            for _ in range(counter):
                reply = random.choice(CRAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            c = b.first_name
            counter = int(MKsr[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(CRAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.1)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

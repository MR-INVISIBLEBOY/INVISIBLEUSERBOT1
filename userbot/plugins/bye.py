import asyncio

from userbot.cmdhelp import CmdHelp
from userbot.utils import admin_cmd

from . import *


@bot.on(admin_cmd(pattern="byeall"))
async def _(event):
    await event.edit("Guys I Gotta Go!")
    await asyncio.sleep(3)
    await event.edit(
        """
╭━━┳╮╱╱╭┳━━━┳━━━┳╮╱╱╭╮
┃╭╮┃╰╮╭╯┃╭━━┫╭━╮┃┃╱╱┃┃
┃╰╯╰╮╰╯╭┫╰━━┫┃╱┃┃┃╱╱┃┃
┃╭━╮┣╮╭╯┃╭━━┫╰━╯┃┃╱╭┫┃╱╭╮
┃╰━╯┃┃┃╱┃╰━━┫╭━╮┃╰━╯┃╰━╯┃
╰━━━╯╰╯╱╰━━━┻╯╱╰┻━━━┻━━━╯
       [⚡️»»»『Pro~Lêɠêɳ̃dẞø†』«««⚡️](https://t.me/LegendBot_Pros)
"""
    )


CmdHelp("byeall").add_command("byeall", NoneType, "Say Bye to U all in anmation").add()

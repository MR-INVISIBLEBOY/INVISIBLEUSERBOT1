from telethon import functions
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotInlineDisabledError as noinline
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import CMD_LIST, bot
from userbot.Config import Config
from userbot.utils import admin_cmd, sudo_cmd

from . import *

mybot = Config.BOT_USERNAME
if mybot.startswith("@"):
    botname = mybot
else:
    botname = f"@{mybot}"

msg = f"""
**โ ๐ป๐๐๐๐๐๐๐๐ข ๐ฐ๐ โ ๏ธ แดส โ ษชษดแด ษช๐ขษชสสแด๐ฑ๐๐ โ**

  โข        [โฅ๏ธ ๐๐๐๐ โฅ๏ธ](https://github.com/MR-INVISIBLEBOY/)
  โข        [โฆ๏ธ Repl โฆ๏ธ]()

  โข  ยฉ๏ธ {Legend_channel} โข
"""


@bot.on(admin_cmd(pattern="repo$"))
@bot.on(sudo_cmd(pattern="repo$", allow_sudo=True))
async def repo(event):
    try:
        legend = await bot.inline_query(botname, "repo")
        await legend[0].click(event.chat_id)
        if event.sender_id == MR_INVISIBLE_OFFICIAL:
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg)


@bot.on(admin_cmd(pattern="help ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="help ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    tgbotusername = botname
    chat = "@Botfather"
    if tgbotusername is not None:
        try:
            results = await event.client.inline_query(tgbotusername, "INVISIBLEBOT_help")
            await results[0].click(
                event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
            )
            await event.delete()
        except noinline:
            legend = await eor(
                event,
                "**Inline Mode is disabled.** \n__Turning it on, please wait for a minute...__",
            )
            async with bot.conversation(chat) as conv:
                try:
                    first = await conv.send_message("/setinline")
                    second = await conv.get_response()
                    third = await conv.send_message(tgbotusername)
                    fourth = await conv.get_response()
                    fifth = await conv.send_message(perf)
                    sixth = await conv.get_response()
                    await bot.send_read_acknowledge(conv.chat_id)
                except YouBlockedUserError:
                    return await legend.edit("Unblock @Botfather first.")
                await legend.edit(
                    f"**Turned On Inline Mode Successfully.** \n\nDo `{l1}invisible` again to get the help menu."
                )
            await bot.delete_messages(
                conv.chat_id,
                [first.id, second.id, third.id, fourth.id, fifth.id, sixth.id],
            )
    else:
        await eor(
            event,
            "**โ ๏ธ ๐ด๐๐๐พ๐ !!** \n๐ฟ๐๐๐๐๐ ๐๐-๐ฒ๐๐๐๐ BOT_TOKEN & BOT_USERNAME on Heroku.",
        )


@bot.on(admin_cmd(pattern="invisible ?(.*)", outgoing=True))
async def yardim(event):
    if event.fwd_from:
        return
    tgbotusername = botname
    input_str = event.pattern_match.group(1)
    if tgbotusername is not None or LEGEND_input == "text":
        results = await event.client.inline_query(tgbotusername, "INVISIBLE-LEGENDBOT_help")
        await results[0].click(
            event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
        )
        await event.delete()
    else:
        await eor(event, "**Check Bot Token And Bot Username In Reveal Var*")

        if input_str in CMD_LIST:
            string = "Commands found in {}:\n".format(input_str)
            for i in CMD_LIST[input_str]:
                string += "  " + i
                string += "\n"
            await event.edit(string)
        else:
            await event.edit(input_str + " is not a valid plugin!")


@bot.on(admin_cmd(pattern="ihelp(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="ihelp(?: |$)(.*)", allow_sudo=True))
async def LEGENDBOTt(event):
    if event.fwd_from:
        return
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await eor(event, str(CMD_HELP[args]))
        else:
            await eor(event, "**โ ๏ธSorry !** \nPlugin ๐๐๐๐ ๐๐ ๐๐๐๐  ๐๐๐๐๐๐ ๐๐๐๐")
    else:
        string = ""
        sayfa = [
            sorted(list(CMD_HELP))[i : i + 5]
            for i in range(0, len(sorted(list(CMD_HELP))), 5)
        ]

        for i in sayfa:
            string += f"`๐`"
            for sira, a in enumerate(i):
                string += "`" + str(a)
                if sira == i.index(i[-1]):
                    string += "`"
                else:
                    string += "`, "
            string += "\n"
        await eor(
            event,
            "Please Specify A Module Name Of Which You Want Info" + "\n\n" + string,
        )


@borg.on(admin_cmd(pattern="config"))  # pylint:disable=E0602
async def _(event):

    if event.fwd_from:

        return

    result = await borg(functions.help.GetConfigRequest())  # pylint:disable=E0602

    result = result.stringify()

    logger.info(result)  # pylint:disable=E0602

    await event.edit("ััโััะฝฯฮท  ะฒฮฑััโ ฯัััะฒฯั ฯฯฯัััโ ะฒั **Invisibleแบรธโ ** ะฒฯั")


CmdHelp("helper").add_command("repo", None, "To Get Repo And Repl Link").add_command(
    "help", None, "To Get Help Menu"
).add_command(
    "op", "<plugin name>", "To Get Detail About Plugin", "op alive"
).add_command(
    "ihelp", "<Pluggin Name>", "To get detail about any plugin"
).add()

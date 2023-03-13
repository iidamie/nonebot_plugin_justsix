from nonebot import on_command
from nonebot.permission import SUPERUSER
from nonebot.matcher import Matcher
from nonebot.internal.adapter import Event

six = on_command("6")


@six.handle()
async def _(matcher: Matcher, _: Event):
    await matcher.finish("6")

sixxx = on_command("666")


@sixxx.handle()
async def _(matcher: Matcher, _: Event):
    await matcher.finish("666")

sixxxx = on_command("6666")


@sixxxx.handle()
async def _(matcher: Matcher, _: Event):
    await matcher.finish("6666")

sixxxxx = on_command("66666")


@sixxxxx.handle()
async def _(matcher: Matcher, _: Event):
    await matcher.finish("666")

sixxxxxx = on_command("666666")


@sixxxxxx.handle()
async def _(matcher: Matcher, _: Event):
    await matcher.finish("666666")
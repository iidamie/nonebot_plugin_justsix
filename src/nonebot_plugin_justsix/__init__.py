from nonebot import on_regex; from nonebot.internal.adapter import Event
@on_regex(r"^6+$", priority=5, block=False).handle()
async def _(event: Event): await on_regex(r"^6+$", priority=5, block=False).finish(event.get_message())

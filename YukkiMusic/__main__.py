import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from YukkiMusic import LOGGER, app, userbot
from YukkiMusic.core.call import Yukki
from YukkiMusic.plugins import ALL_MODULES
from YukkiMusic.utils.database import get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("YukkiMusic").error(
            "Tanımlı Yardımcı İstemci Yok!.. İşlemden Çık."
        )
        return
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("YukkiMusic.plugins" + all_module)
    LOGGER("Yukkimusic.plugins").info(
        "Modüller Başarıyla Alındı "
    )
    await userbot.start()
    await Yukki.start()
    try:
        await Yukki.stream_call(
            "http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("YukkiMusic").error(
            "[HATA] - \n\nLütfen Logger Grubunuzun Sesli Aramasını açın. Günlük grubunuzda sesli aramayı asla kapatmadığınızdan/sonlandırmadığınızdan emin olun"
        )
        sys.exit()
    except:
        pass
    await Yukki.decorators()
    LOGGER("YukkiMusic").info("Yukki Müzik Botu Başarıyla Başladı")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("YukkiMusic").info("Yukki Müzik Botu durduruluyor! Hoşçakal")

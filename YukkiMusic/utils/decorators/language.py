# Aşağıdaki yerleri tr yaptım otomatik Tr görmesi için sorun olursa (en) yapınız. 

from strings import get_string
from YukkiMusic.utils.database import get_lang, is_commanddelete_on


def language(mystic):
    async def wrapper(_, message, **kwargs):
        if await is_commanddelete_on(message.chat.id):
            try:
                await message.delete()
            except:
                pass
        try:
            language = await get_lang(message.chat.id)
            language = get_string(language)
        except:
            language = get_string("tr")
        return await mystic(_, message, language)

    return wrapper


def languageCB(mystic):
    async def wrapper(_, CallbackQuery, **kwargs):
        try:
            language = await get_lang(CallbackQuery.message.chat.id)
            language = get_string(language)
        except:
            language = get_string("tr")
        return await mystic(_, CallbackQuery, language)

    return wrapper

import asyncio
import contextlib
import logging
from aiogram.types import ChatJoinRequest, FSInputFile
from aiogram import Bot, Dispatcher, F, types

BOT_TOKEN = '6584524444:AAHO2uABbSYohhhJFsIAqZZ809Or3NhqQcY'
CHANNEL_ID = -1001497047339
ADMIN_ID = 666575005

async def approve_request(chat_join: ChatJoinRequest, bot: Bot):
    msg = f'''Новый способ абуза 1WIN⤵️
    
https://t.me/bonusVcasino1'''
    
    await bot.send_photo(chat_id=chat_join.from_user.id, photo=FSInputFile(path='smm.jpeg'), caption=msg)

    
async def start():
    logging.basicConfig(level=logging.DEBUG,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                                "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")
    
    bot: Bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.chat_join_request.register(approve_request, F.chat.id == CHANNEL_ID)

    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    except Exception as ex:
        logging.error(f'[Exception] - {ex}', exc_info=True)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    with contextlib.suppress(KeyboardInterrupt, SystemExit):
        asyncio.run(start())

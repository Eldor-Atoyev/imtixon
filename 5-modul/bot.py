import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from db import  Session, User, Message_

TOKEN = "6465163329:AAETwaKyIGdDGdm4lO_tPdYxA3VDANOAJkQ"


dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    session = Session()
    user_list = session.query(User).filter(User.user_telegram_id == str(message.from_user.id)).first()
    if not user_list:

        user_telegram_id = message.from_user.id
        username = message.from_user.username
        created = message.date

        user = User(user_telegram_id=user_telegram_id, username=username, created=created)
        session = Session()
        session.add(user)
        session.commit()
        await message.reply("Barcha ma'lumotlar saqlanyapti ")
    else:
        await message.answer('Xush kelibsiz')





@dp.message()
async def user_chat_handler(message: Message) -> None:
    user_id = str(message.from_user.id)
    text = message.text
    created = message.date
    mes = Message_(user_id=user_id, text=text, created=created)
    session = Session()
    session.add(mes)
    session.commit()
    await message.answer(f"{message.from_user.username} saved message")


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())


import functools
import requests

from aiogram import Bot, Dispatcher, F, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, InputFile
from aiogram import types

TOKEN = "7013823926:AAF84HgnDvde25cwE2VablqSLTIJhpDinHg"

dp = Dispatcher()


@functools.cache
def bot() -> Bot:
    return Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))


@dp.message(Command("post"))
async def photo_message(message: Message):
    chat_id = message.from_user.id
    await bot().send_message(
        chat_id, f"Привет, {message.from_user.full_name}, лови картинку:"
    )
    await bot().send_photo(
        chat_id,
        photo=types.FSInputFile("photo/cam_1.png"),
        caption="camera_1",
        parse_mode=ParseMode.HTML,
    )


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(
        f"Привет, {html.bold(message.from_user.full_name)}<b> | Твой id: {message.from_user.id}  </b>"
    )


# def send_tg(user_email, course: str):
#     requests.post(
#             f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",
#             json={"chat_id": tg_user_id, "text": f'Вы только что приобрели новый курс: "{course}"'},
#         )


async def main() -> None:
    await dp.start_polling(bot())


from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from decouple import config


TOKEN = config("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message) -> None:
    await bot.send_message(message.chat.id, f"Hello User {message.from_user.full_name}")


@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message) -> None:
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton("Дальше", callback_data="next_button1")
    markup.add(button)
    quiestion = "Кто был первым в мире программистом?"
    answers = [
        "Ilon Mask",
        "Gagarin",
        "Ada Lavleis",
        "Adham Soliev",
        "Mark Cuckerberg",
    ]
    await message.answer_poll(
        question=quiestion,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Я думал ты умный!",
        open_period=10,
        reply_markup=markup
    )


@dp.callback_query_handler(text="next_button1")
async def quiz_2(callback: types.CallbackQuery):
    quiestion = "Что такое PYTHON?"
    answers = [
        "Змея",
        "Игрушка",
        "Язык програмирования",
        "Новый сленг",
        "Школа программированния",
        "Межгалактическая планета"
    ]
    await callback.message.answer_poll(
        question=quiestion,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="ТЫ ТУПОЙ ЧТОЛИ!",
        open_period=10,
    )


@dp.message_handler(commands=['mem'])
async def send_mem(message: types.Message):
    await bot.send_photo(message.chat.id, photo=open('img/img.jpg', 'rb'))


@dp.message_handler()
async def echo(message: types.Message) -> None:
    if message.text.isdigit():
        await message.answer(int(message.text) ** 2)
    else:
        await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)4

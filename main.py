import random

from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from random import choices
from tooken import BOT_TOKEN


prediction = ['Насколько я понимаю, да',
              'Спросите еще раз позже.',
              'Лучше не говорить вам сейчас.',
              'Сейчас не могу предсказать.',
              'Сосредоточься и спроси еще раз.',
              'Не рассчитывайте на это.',
              'Это точно.',
              'Это определенно так.',
              'Скорее всего.',
              'Мой ответ - нет.',
              'Мои источники говорят, что нет.',
              'Перспективы не очень хорошие.',
              'Перспективы хорошие.',
              'Ответить туманно, попробуйте еще раз.',
              'Знаки указывают на "да".',
              'Очень сомнительно.',
              'Без сомнения.',
              'ДА.',
              'Да, определенно.',
              'Вы можете положиться на это.']



bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Purpl-bot\n Спроси у меня что-нибудь!')


@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебе предсказание '
        'на твое будущее'
    )


@dp.message()
async def send_echo(message: Message):
    await message.reply(text=random.choice(prediction))


if __name__ == '__main__':
    dp.run_polling(bot)

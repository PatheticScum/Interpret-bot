from aiogram import types

from aiogram.dispatcher.filters import Text

from keyboards.default.translation import inter
from loader import dp
from translate import Translator


@dp.message_handler(commands='inter')
async def bot_help(message: types.Message):
    await message.answer('Choose language that you wanted to translate',
                         reply_markup=inter)


try:

    @dp.message_handler(Text(equals=['UZ']))
    async def uz(message: types.Message):
        result = message.text
        translator = Translator(to_lang="UZ")
        translation = translator.translate(result)
        await message.answer(translation)


    @dp.message_handler(Text(equals=['RU']))
    async def ru(message: types.Message):
        result = message.text
        translator = Translator(to_lang="RU")
        translation = translator.translate(result)
        await message.answer(translation)


    @dp.message_handler(Text(equals=['EN']))
    async def en(message: types.Message):
        result = message.text
        translator = Translator(to_lang="EN")
        translation = translator.translate(result)
        await message.answer(translation)
except Exception as e:
    await msg.answer("Send the link in order to download the video 🔗:")

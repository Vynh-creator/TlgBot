from aiogram import F, Router, types, Bot
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
import app.keyboads as kb
import app.database.requests as rq

router = Router()
# router.message.middleware(TestMiddleWare())




# class Reg(StatesGroup):
#   name = State()
#  number = State()

async def send_start_message(message: Message):
    await message.answer(
        "Добро пожаловать к нам в телеграмм бот!\n Мы компания Робот и я если вы хотите вы можете записаться к нам на занятия",
        reply_markup=kb.main)


@router.message(CommandStart())
async def cmd_start(message: Message):
    await send_start_message(message)


@router.callback_query(F.data == 'to_main')
async def to_main(callback: CallbackQuery):
    await callback.answer()
    await send_start_message(callback.message)


@router.message(F.text == "Информация о нас")
async def inf_about_club(message: Message):
    await message.answer("Здесь вы можете посмотреть все о нашем клубе")


@router.message(F.text == "Наши награды")
async def rewards(message: Message):
    await message.answer("У нас есть много серьезных наград")

@router.message(F.text == "Запись")
async def write_on(message: Message):
    await message.answer("Выберите день записи",reply_markup=await kb.days())

@router.message(F.data.startswith("day_"))
async def choose_time(callback:CallbackQuery):
    await callback.message.answer("Выберите время", reply_markup=await kb.time(callback.data.split("_")[1]))
# @router.message(Command("reg"))
# async def reg1(message: Message, state: FSMContext):
#   await state.set_state(Reg.name)
#  await message.answer("Введите ваше имя")

# @router.message(Reg.name)
# async def reg_two(message: Message, state: FSMContext):
#   await state.update_data(name=message.text)
#  await state.set_state(Reg.number)
#  await message.reply("Введите номер", reply_markup=kb.req_numb)

# @router.message(Reg.number, F.contact)
# async def reg3(message: types.Message, state: FSMContext):
#   await state.update_data(number=message.contact.phone_number)
#  data = await state.get_data()
# await message.answer(f"Спасибо, регистрация завершена Имя: {data['name']}, Номер: {data['number']}")
# await state.clear()
# await message.answer("Регистрация завершена.", reply_markup=types.ReplyKeyboardRemove())

# @router.message(F.text == 'Каталог')
# async def catalog(message: Message):
#   await message.answer("Выберите категорию товара", reply_markup=await kb.categories())


# @router.callback_query(F.data.startswith("category_"))
# async def category(callback: CallbackQuery):
#   await callback.answer("Вы выбрали категорию")
#  await callback.message.answer("Выберите товар по категории",
#            reply_markup=await kb.items(callback.data.split("_")[1]))


# @router.callback_query(F.data.startswith("item_"))
# sync def category(callback: CallbackQuery):
#   item_data = await rq.get_item_inf(callback.data.split("_")[1])
#  await callback.answer("Вы выбрали товар")
# await callback.message.answer(
#    f"Название: {item_data.name},\n Описание: {item_data.description},\n цена: {item_data.price}$",
#   reply_markup=await kb.items(callback.data.split("_")[1]))

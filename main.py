import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder

TOKEN = "8775428797:AAGtztSrEbg8-ahyWJlVnDIEgpKjX5WeZlI"

bot = Bot(token=TOKEN)
dp = Dispatcher()

def get_main_menu():
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="📱 Приложение [Все игры]", web_app=types.WebAppInfo(url="https://google.com")))
    builder.row(types.InlineKeyboardButton(text="🦅 Товары PUBG MOBILE", callback_data="pubg_shop"))
    builder.row(
        types.InlineKeyboardButton(text="🎁 Промокоды", callback_data="promocodes"),
        types.InlineKeyboardButton(text="💬 Информация", callback_data="info")
    )
    builder.row(types.InlineKeyboardButton(text="👥 Реферальная система", callback_data="referral"))
    builder.row(types.InlineKeyboardButton(text="⭐ Пополнить Telegram stars", callback_data="stars_topup"))
    builder.row(types.InlineKeyboardButton(text="🌐 Свободный интернет", callback_data="free_internet"))
    return builder.as_markup()

@dp.message(CommandStart())
async def start_command(message: types.Message):
    photo_url = "https://picsum.photos"
    caption_text = "👋 **Добро пожаловать в магазин @Metroshopfrest_bot!**\n\nИспользуйте меню ниже для навигации:"
    await message.answer_photo(photo=photo_url, caption=caption_text, parse_mode="Markdown", reply_markup=get_main_menu())

@dp.callback_query(lambda c: c.data == "pubg_shop")
async def process_pubg_shop(callback_query: types.CallbackQuery):
    items_builder = InlineKeyboardBuilder()
    items_builder.row(types.InlineKeyboardButton(text="💵 60 UC — 120₽", callback_data="buy_60uc"))
    items_builder.row(types.InlineKeyboardButton(text="💵 325 UC — 600₽", callback_data="buy_325uc"))
    items_builder.row(types.InlineKeyboardButton(text="💵 660 UC — 1100₽", callback_data="buy_660uc"))
    items_builder.row(types.InlineKeyboardButton(text="⬅️ Назад в меню", callback_data="back_to_main"))
    await callback_query.message.edit_caption(caption="🛒 **Выберите количество UC для покупки:**", parse_mode="Markdown", reply_markup=items_builder.as_markup())
    await callback_query.answer()

@dp.callback_query(lambda c: c.data == "back_to_main")
async def back_to_main(callback_query: types.CallbackQuery):
    caption_text = "👋 **Добро пожаловать в магазин @Metroshopfrest_bot!**\n\nИспользуйте меню ниже для навигации:"
    await callback_query.message.edit_caption(caption=caption_text, parse_mode="Markdown", reply_markup=get_main_menu())
    await callback_query.answer()

@dp.callback_query(lambda c: c.data in ["promocodes", "info", "referral", "stars_topup", "free_internet"])
async def process_other_buttons(callback_query: types.CallbackQuery):
    await callback_query.answer(text="⚠️ Этот раздел сейчас находится в разработке!", show_alert=True)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    print("🚀 Бот @Metroshopfrest_bot успешно запущен и ждет команд!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

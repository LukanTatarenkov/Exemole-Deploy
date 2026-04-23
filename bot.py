import asyncio
import random
import logging
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# --- КОНФІГУРАЦІЯ ---
TOKEN = "ВАШ_ТОКЕН_ТУТ"  # Отримайте у @BotFather

# --- ДАНІ ТА ЛОГІКА ---
QUOTES = [
    "Служба Імператору — сама по собі нагорода.",
    "Знання — це сила, оберігай її.",
    "Навіть той, хто нічого не має, може віддати своє життя.",
    "Розум, що сумнівається — порожня фортеця з відкритими брамами.",
    "Смерть — це не кінець, це виконання обов'язку."
]

def get_dice_result(roll):
    results = {
        1: "💀 Провал! Осечка болтера. Ви впали в очах Омнисії.",
        2: "💢 Слабкий удар. Броня єретика витримала.",
        3: "🛡️ Посередньо. Лінія фронту тримається.",
        4: "🎯 Влучний постріл! За Святу Терру!",
        5: "🔥 Нищівна лють! Вороги розлітаються на шматки.",
        6: "🦅 КРИТИЧНИЙ УСПІХ! Імператор спрямовує вашу руку!"
    }
    return results.get(roll)

# --- КЛАВІАТУРА ---
def main_kb():
    builder = ReplyKeyboardBuilder()
    builder.button(text="📜 Думка дня")
    builder.button(text="🎲 Кинути кубик")
    builder.button(text="🛡️ Статус")
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)

# --- ОБРОБНИКИ ПОДІЙ ---
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "🔮 **АВТОРИЗАЦІЯ ПРИЙНЯТА**\n\n"
        "Вітаю, служителю. Я — системний когітатор вашого підрозділу.\n"
        "Пам'ятай: неуцтво — це благословення, але накази мають виконуватися.",
        reply_markup=main_kb(),
        parse_mode="Markdown"
    )

@dp.message(F.text == "📜 Думка дня")
async def send_quote(message: types.Message):
    quote = random.choice(QUOTES)
    await message.answer(f"📖 *Запис у літописі:*\n\n`{quote}`", parse_mode="Markdown")

@dp.message(F.text == "🎲 Кинути кубик")
async def roll_dice(message: types.Message):
    roll = random.randint(1, 6)
    res_text = get_dice_result(roll)
    await message.answer(f"🎲 На кубику: **{roll}**\n\n{res_text}", parse_mode="Markdown")

@dp.message(F.text == "🛡️ Статус")
async def send_status(message: types.Message):
    await message.answer(
        "📊 **Діагностика систем:**\n"
        "└ Боєзапас: 89%\n"
        "└ Рівень віри: **НЕПОХИТНИЙ**\n"
        "└ Загроза ксеносів: Присутня\n\n"
        "Слава Богу-Імператору!"
    )

# --- ЗАПУСК ---
async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=TOKEN)
    print("⚡ Когітатор активовано. Бот готовий до служби!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n🔴 Зв'язок з Варпом перервано.")
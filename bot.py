from aiogram import executor
from dispatcher import dp
import handlers

print("БОЛЬШЕ БОТОВ НА CONFF.ORG")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
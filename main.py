import requests
from datetime import datetime
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from fastapi import FastAPI, Request
app = FastAPI()

token = '5031087182:AAFYXpAf6tzKhbz82x_fz-u3io9nUi2UQsg'

bot = Bot(token=token)
dp = Dispatcher(bot)

def get_data():
	req = requests.get('https://yobit.net/api/3/ticker/btc_usd')
	res = req.json()
	print(res)
	sell_price = res['btc_usd']['sell']
	print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\n Sell BTC price: {sell_price}")
	res = f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTC price: $ {sell_price}"
	return res


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
	await bot.send_message(message.from_user.id, 'Hello friend! Wright the \'price\' to find out the cost of BTC to USD')


@dp.message_handler()
async def bot_message(message: types.Message):
	if message.chat.type == 'private':
		if message.text == 'price':
			res = get_data()
			await bot.send_message(message.from_user.id, res)
	else:
		await bot.send_message(message.from_user.id, 'Wright the \'price\' to find out the cost of BTC to USD')


if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)


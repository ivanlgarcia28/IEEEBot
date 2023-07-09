# Importing required libraries
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import json
from config import *

# Put the token that you received from BotFather in the quotes
bot = Bot(token=TELEGRAM_TOKEN)

# Initializing the dispatcher object
dp = Dispatcher(bot)

# JSON file
with open('info.json') as f:
    data = json.load(f)

# Defining and adding buttons
eventsButton = InlineKeyboardButton(text="Events", callback_data="events_button")
fundingsButton = InlineKeyboardButton(text="Fundings", callback_data="fundings_button")
remindersButton = InlineKeyboardButton(text="Reminders", callback_data="reminders_button")
keyboard_inline = InlineKeyboardMarkup().add(eventsButton, fundingsButton, remindersButton)

# Message handler for the /button1 command
@dp.message_handler(commands=['start'])
async def check(message: types.Message):
	await message.reply("Hey you, I'm IEEE R9 bot 😁. How can I help you?", reply_markup=keyboard_inline)

# Callback query handler for the inline keyboard buttons
@dp.callback_query_handler(text=["events_button", "fundings_button", "reminders_button"])
async def check_button(call: types.CallbackQuery):
	# Checking which button is pressed and respond accordingly
	if call.data == "events_button":
		array_of_events = [
            data['events'][0]['name'],
            data['events'][1]['name'],
            data['events'][2]['name']
        ]
		cantEvents = len(array_of_events)
		for i in range(cantEvents):
			Button1 = InlineKeyboardButton(text=array_of_events[0], callback_data="ieeextreme_button")
			Button2 = InlineKeyboardButton(text=array_of_events[1], callback_data="sactraining_button")
			Button3 = InlineKeyboardButton(text=array_of_events[2], callback_data="r8africansyp_button")
		# 	match i:
		# 		case "1":
		# 			Button1 = InlineKeyboardButton(text=array_of_events[i], callback_data=array_of_events[i] + "_button")
		# 		case "2":
		# 			Button2 = InlineKeyboardButton(text=array_of_events[i], callback_data=array_of_events[i] + "_button")
		keyboard1_inline = InlineKeyboardMarkup().add(Button1, Button2, Button3)
		await call.message.answer(text= "Events list: ", reply_markup=keyboard1_inline)

	elif call.data == "reminders_button":
		array_of_reminders = [
			data['reminders'][0]['name'],
			data['reminders'][1]['name']
		]
		cantReminders = len(array_of_reminders)
		for i in range(cantReminders):
			Button1 = InlineKeyboardButton(text=array_of_reminders[0], callback_data="ieeextreme_button")
			Button2 = InlineKeyboardButton(text=array_of_reminders[1], callback_data="sactraining_button")
		keyboard1_inline = InlineKeyboardMarkup().add(Button1, Button2)
		await call.message.answer(text= "Reminders list: ", reply_markup=keyboard1_inline)

		@dp.callback_query_handler(text=["ieeextreme_button", "sactraining_button"])
		async def reminders_button(call: types.CallbackQuery):
			print('Entre ieeextreme_button y')
			# if call.data == "ieeextreme_button":
			# 	print('Entre ieeextreme_button')
			# elif call.data == "sactraining_button":
			# 	print('Entre sactraining_button')	

	elif call.data == "fundings_button":
		await call.message.answer("Hi! This is the fundings keyboard button.")

	# Notify the Telegram server that the callback query is answered successfully
	await call.answer()
	
# Start the bot
executor.start_polling(dp)
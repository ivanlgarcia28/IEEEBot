# Importing required libraries
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import json
from config import *
from telegram.constants import ParseMode

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
resourcesButton = InlineKeyboardButton(text="Resources", callback_data="resources_button")
keyboard_inline = InlineKeyboardMarkup().add(eventsButton, fundingsButton, remindersButton, resourcesButton)

# Message handler for the /button1 command
@dp.message_handler(commands=['start'])
async def check(message: types.Message):
	await message.reply("Hey you, I'm IEEE bot from IEEE Argentina Section 😁. How can I help you?", reply_markup=keyboard_inline)

# Callback query handler for the inline keyboard buttons
@dp.callback_query_handler(text=["events_button", "fundings_button", "reminders_button", "resources_button"])
async def check_button(call: types.CallbackQuery):
	# Checking which button is pressed and respond accordingly
	if call.data == "events_button":
		array_of_events = data['events']
		button_events = []
		markup = types.InlineKeyboardMarkup()
		caption = "<b>Events list, choose one for more information!</b>"
		for key, value in array_of_events.items():
			button_events.append(key)
			markup.add(InlineKeyboardButton(text=value['name'], callback_data=key))

		await call.message.answer(text=caption, parse_mode='HTML' , reply_markup=markup)

		@dp.callback_query_handler(text=button_events)
		async def eventsdescription_button(call: types.CallbackQuery):
			await call.message.answer(text=array_of_events[call.data]["name"], parse_mode='HTML')
			await call.message.answer(text=array_of_events[call.data]["description"])
			await call.message.answer(text=array_of_events[call.data]["url"])
	elif call.data == "reminders_button":
		array_of_reminders = data['reminders']
		button_reminders = []
		markup1 = types.InlineKeyboardMarkup()
		caption1 = "<b>Reminders list, choose one for more information!</b>"
		for key, value in array_of_reminders.items():
			button_reminders.append(key)
			markup1.add(InlineKeyboardButton(text=value['name'], callback_data=key))

		await call.message.answer(text=caption1, parse_mode='HTML', reply_markup=markup1)

		@dp.callback_query_handler(text=button_reminders)
		async def remindersdescription_button(call: types.CallbackQuery):
			await call.message.answer(text=array_of_reminders[call.data]["name"])
			await call.message.answer(text=array_of_reminders[call.data]["description"])
			await call.message.answer(text=array_of_reminders[call.data]["description"])

	elif call.data == "fundings_button":
		array_of_fundings = data['fundings']
		button_fundings = []
		markup2 = types.InlineKeyboardMarkup()
		caption2 = "<b>Fundings list, choose one for more information!</b>"
		for key, value in array_of_fundings.items():
			button_fundings.append(key)
			markup2.add(InlineKeyboardButton(text=value['name'], callback_data=key))

		await call.message.answer(text=caption2, parse_mode='HTML' , reply_markup=markup2)

		@dp.callback_query_handler(text=button_fundings)
		async def fundingsdescription_button(call: types.CallbackQuery):
			await call.message.answer(text=array_of_fundings[call.data]["name"])
			await call.message.answer(text=array_of_fundings[call.data]["description"])
			await call.message.answer(text=array_of_fundings[call.data]["url"])
	elif call.data == "resources_button":
		array_of_resources = data['resources']
		button_resources = []
		markup3 = types.InlineKeyboardMarkup()
		caption3 = "<b>Resourcers list, choose one for more information!</b>"
		for key, value in array_of_resources.items():
			button_resources.append(key)
			markup3.add(InlineKeyboardButton(text=value['name'], callback_data=key))

		await call.message.answer(text=caption3, parse_mode='HTML' , reply_markup=markup3)

		@dp.callback_query_handler(text=button_resources)
		async def resourcesdescription_button(call: types.CallbackQuery):
			await call.message.answer(text=array_of_resources[call.data]["name"])
			await call.message.answer(text=array_of_resources[call.data]["description"])
			await call.message.answer(text=array_of_resources[call.data]["url"])
	# Notify the Telegram server that the callback query is answered successfully
	await call.answer()
	
# Start the bot
executor.start_polling(dp)

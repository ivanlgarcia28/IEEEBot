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
		cantEvents = len(array_of_events)
		markup = types.InlineKeyboardMarkup()

		for i in range(cantEvents):
			event = array_of_events[i]
			markup.add(InlineKeyboardButton(text=event['name'], callback_data=f'{event["id"]}_button'))
		await call.message.answer(text='Events' , reply_markup=markup)

		@dp.callback_query_handler(text=["ieeextreme_17_button", "rnr_chile_button"])
		async def eventsdescription_button(call: types.CallbackQuery):
		# Checking which button is pressed and respond accordingly
			if call.data == "ieeextreme_17_button":
				await call.message.answer(text="1st")

	elif call.data == "reminders_button":
		array_of_reminders = data['reminders']
		cantReminders = len(array_of_reminders)
		markup1 = types.InlineKeyboardMarkup()

		for i in range(cantReminders):
			reminder = array_of_reminders[i]
			markup1.add(InlineKeyboardButton(text=reminder['name'], callback_data=f'{reminder["id"]}_button'))
		await call.message.answer(text='Reminders', reply_markup=markup1)

	elif call.data == "fundings_button":
		array_of_fundings = data['fundings']
		cantFundings = len(array_of_fundings)
		markup2 = types.InlineKeyboardMarkup()

		for i in range(cantFundings):
			funding = array_of_fundings[i]
			markup2.add(InlineKeyboardButton(text=funding['name'], callback_data=f'{funding["id"]}_button'))
		
		await call.message.answer(text='Fundings', reply_markup=markup2)
	elif call.data == "resources_button":
		array_of_resources = data['resources']
		cantResources = len(array_of_resources)
		markup3 = types.InlineKeyboardMarkup()

		for i in range(cantResources):
			resources = array_of_resources[i]
			markup3.add(InlineKeyboardButton(text=resources['name'], callback_data=f'{resources["id"]}_button'))
	
		await call.message.answer(text='Resources', reply_markup=markup3)
	
	# Notify the Telegram server that the callback query is answered successfully
	await call.answer()
	
# Start the bot
executor.start_polling(dp)
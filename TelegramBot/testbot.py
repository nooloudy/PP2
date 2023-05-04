import telebot
from telebot import types
import random
import psycopg2

connection = psycopg2.connect(
    host = "localhost",
    user = "postgres" ,
    password = "nooloudy",
    database = "postgres"
)
connection.autocommit = True
cursor = connection.cursor()
def createTable():
    cursor.execute('CREATE TABLE TELEBOT(id serial PRIMARY KEY,name varchar(100) NOT NULL,surname varchar(100) NOT NULL,age varchar(100) NOT NULL, address varchar(100) NOT NULL);')

def inputData(name,surname,age,address):

    cursor.execute('INSERT INTO postgres.public.telebot("name","surname","age","address") VALUES (%s,%s,%s,%s);' , (name,surname,age,address))

def delete_information(NamePerson):
    
    cursor.execute(f''' DELETE FROM postgres.public.telebot WHERE "name" = '{NamePerson}' ''')

def delete_all_information():
    cursor.execute(' DELETE FROM postgres.public.telebot ')

TOKEN = '6097379695:AAH0pi3cO6dQcMS3-Mevud1l2y6u4nmuPHI' #bot token fцrom @BotFather
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands = ['start'])
def start(message):
    mess_start = f'Welcome, <b>{message.from_user.first_name}</b>,write "/help" that to see all commands'
    bot.send_message(message.chat.id, mess_start, parse_mode = 'html')
    
@bot.message_handler(commands = ['help'])
def help_(message):
    mess_start = f'What do you want to do?\n\
          1. /start - start all over again\n\
          2. /help - all commands\n\
          3. /chat - little chat with the bot\n\
          4. /regData - input Data into the databases\n\
          5. /deleteData - delete the selected data \n\
          6. /deleteAllData - delete all data on databases\n\
          7. /dataBases - shows all data on the database\n\
            '
    bot.send_message(message.chat.id, mess_start, parse_mode = 'html')
@bot.message_handler(commands = ['regData'])

def inputdata(message):
    bot.send_message(message.chat.id, f'Please, write your name: ', parse_mode = 'html')
    bot.register_next_step_handler(message,nname)

def nname(message):
    global name;
    name = message.text
    bot.send_message(message.chat.id, 'Please, write your surname: ', parse_mode = 'html')
    bot.register_next_step_handler(message,surname)

def surname(message):
    global surname;
    surname = message.text
    bot.send_message(message.chat.id, 'Please, write your age: ', parse_mode = 'html')
    bot.register_next_step_handler(message,Age)

def Age(message):
    global age;
    age = message.text
    bot.send_message(message.chat.id, 'Please, write your address: ', parse_mode = 'html')
    bot.register_next_step_handler(message, Address)

def Address(message):
    global address;
    address = message.text
    keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
    key_yes = types.InlineKeyboardButton(text='Yes', callback_data='yes'); #кнопка «Да»
    keyboard.add(key_yes); #добавляем кнопку в клавиатуру
    key_no= types.InlineKeyboardButton(text='No', callback_data='no');
    keyboard.add(key_no);
    question = 'Your ' + str(name)+' '+str(surname)+', your age is '+str(age)+' and your address '+str(address)+'?'
    bot.send_message(message.from_user.id, text = question, reply_markup= keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes": #call.data это callback_data, которую мы указали при объявлении кнопки
        inputData(name,surname,age,address)#код сохранения данных, или их обработки
        bot.send_message(call.message.chat.id, 'Remember it😊');
    elif call.data == "no":
        bot.send_message(call.message.chat.id, 'Please, write "/regData" and Rewrite your details', parse_mode= 'html')

@bot.message_handler(commands = ['deleteData'])
def deleteData(message):
    question = 'Please, write the name of data, which you want to delete: '
    bot.send_message(message.chat.id, question, parse_mode= 'html')
    bot.register_next_step_handler(message, deleteData2)
def deleteData2(message):
    global NAME_DELETE;
    NAME_DELETE = message.text
    
    question = 'Your definitely need to delete this data '+str(NAME_DELETE)+'?\nIf you agree send me + or not send me -'
    bot.send_message(message.from_user.id, text = question, parse_mode = 'html')
    bot.register_next_step_handler(message, agree)

def agree(message):
    global Agree;
    Agree = message.text
    if message.text == "+":
            delete_information(NAME_DELETE)
            bot.send_message(message.chat.id, 'Succesfully removed😊',parse_mode = 'html')

    elif message.text == "-":
        bot.send_message(message.chat.id, 'Please, write "/deleteData"  and Rewrite your details or write "/help"', parse_mode= 'html')


@bot.message_handler(commands = ['deleteAllData'])
def deleteAllData(message):

    question = 'Yout definitely want to delete all data?\nIf you agree send me + or not send me -'
    bot.send_message(message.from_user.id, text = question, parse_mode = 'html')
    bot.register_next_step_handler(message,agree2)

def agree2(message):
    global Agree2;
    Agree2 = message.text
    if Agree2 == "+": #call.data это callback_data, которую мы указали при объявлении кнопки
        delete_all_information()#код сохранения данных, или их обработки
        bot.send_message(message.chat.id, 'Succesfully deleted all data😊',parse_mode = 'html');
    elif Agree2 == "-":
        bot.send_message(message.chat.id, 'Please, write "/deleteAllData" and Rewrite your confirmation or write /help', parse_mode= 'html')

    

@bot.message_handler(commands = ['dataBases'])
def all_information(message):
    cursor.execute(' SELECT * FROM postgres.public.telebot ')
    data = cursor.fetchall()
    for res in data:
        dt = 'Name: ' + str(res[1]) + "\n" + 'Surname: ' + str(res[2]) + "\n" + "Age: " + str(res[3]) + "\n" + "Address: " + str(res[4]) + "\n" 
        bot.send_message(message.chat.id, dt)
    
@bot.message_handler(commands = ['chat'])
def button(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🎲 Random number")
    item2 = types.KeyboardButton("😊 How are you?")

    markup.add(item1, item2)
 
    bot.send_message(message.chat.id, "Choose anything, {0.first_name}!\n".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def chating(message):
    if message.chat.type == 'private':
        if message.text == '🎲 Random number':
            bot.send_message(message.chat.id, str(random.randint(0,10)))
        elif message.text == '😊 How are you?':
            markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
            item1 = types.KeyboardButton("Good")
            item2 = types.KeyboardButton("Bad")
 
            markup.add(item1, item2)
 
            bot.send_message(message.chat.id, 'Not bad, are you?', reply_markup=markup)
        
            bot.register_next_step_handler(message, Answer)

def Answer(message):
    global answer;
    answer = message.text
    if message.chat.type == 'private':
        if answer == 'Good':
            bot.send_message(message.chat.id, 'Good 😊')
        elif answer == 'Bad':
            bot.send_message(message.chat.id, 'I condulance😢')

bot.polling(none_stop = True)
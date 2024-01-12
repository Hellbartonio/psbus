# Telegram @PSBus_bot
import logging
from telegram.ext import Updater, CommandHandler
from datetime import date, datetime

# Timezone for pythonanywhere server
import os, pytz # os нужен и для переменной окружения, pytz для timezone

telegram_token = os.getenv('TELEGRAM_TOKEN')
# heroku_url = 'https://psbus-bot.herokuapp.com/' # для Heroku
heroku_url = 'https://psbus-dev-tesa.1.ie-1.fl0.io' # для FL0
updater = Updater(token=telegram_token, use_context=True)
dispatcher = updater.dispatcher

# logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Отправь /help для списка возможностей")

def bus(update, context):
    today = date.today()
    weekday = today.weekday() # 0-4 будни, 5-6 выходные
    time = datetime.now(pytz.timezone(os.getenv('TZ'))).time().strftime("%H:%M:%S")[:-3]

    nextbusfromIlyicha = None
    nextbustoIlyicha = None
    nextbusfromPaveletskaya = None
    nextbustoPaveletskaya = None
    nextbusfromProletarskaya = None
    nextbustoProletarskaya = None

# От метро пл. Ильича
    fromsub_workdays = [
    '07:35', '07:45', '08:10', '08:15', '08:20', '08:30',
    '08:40', '08:45', '08:47', '08:50', '09:30', '09:40',
    '10:20', '10:40', '11:20', '11:50', '12:30', '13:20',
    '13:50', '14:20', '14:50', '15:20', '15:50', '16:25',
    '16:55', '17:35', '20:30']
    fromsub_weekends = ['08:15', '08:45', '20:30']

# К метро пл. Ильича
    tosub_workdays = [
    '09:15', '10:00', '10:30', '11:00', '11:30', '12:00',
    '13:00', '13:30', '14:00', '14:30', '15:00', '15:30'
    ]
    tosub_monthu = [
    '16:10', '16:40', '17:15', '18:05', '18:07', '18:10',
    '18:20', '18:30', '18:40', '18:50', '19:05', '19:20',
    '19:30', '20:00', '20:10', '20:20', '20:50', '21:15',
    '22:00'
    ]
    tosub_fri = [
    '15:50', '16:10', '16:50', '16:52', '17:00', '17:10',
    '17:25', '17:30', '17:35', '17:45', '18:05', '18:15',
    '18:30', '18:45', '19:15', '19:45', '20:10', '20:20',
    '20:50', '21:15', '22:00'
    ]
    tosub_weekends = ['09:15', '18:15', '21:10']

# От метро Павелецкая
    fromPaveletskaya = [
    '07:40',
    '08:00', '08:15', '08:45',
    '09:15', '09:50',
    '10:40',
    '11:00', '11:30',
    '12:00', '12:30',
    '13:00', '13:30',
    '14:00', '14:30',
    '15:00', '15:30',
    '16:00', '16:30',
    '17:00', '17:15', '17:25', '17:50', 
    '18:35',
    '19:10', '19:50'
    ]

# К метро Павелецкая
    toPaveletskaya = [
    '08:00', '08:30',
    '09:00', '09:35',
    '10:15',
    '11:00', '11:30',
    '12:00', '12:30',
    '13:00', '13:30',
    '14:00', '14:30',
    '15:00', '15:30',
    '16:00', '16:30', '16:55', 
    '17:10', '17:35',
    '18:10',
    '19:30'
    ]

# От метро Пролетарская
    fromProletarskaya = [
    '07:50',
    '08:00', '08:05', '08:10', '08:15', '08:20', '08:25', '08:30', '08:35', '08:40', '08:45', '08:50', '08:55',
    '09:00', '09:05', '09:10', '09:15', '09:20', '09:25', '09:30', '09:35', '09:40', '09:45', '09:50', '09:55',
    '10:00', '10:05', '10:10', '10:15', '10:20', '10:25', '10:30', '10:35', '10:40', '10:45', '10:50', '10:55',
    '11:00', '11:30',
    '12:00', '12:30',
    '13:00', '13:30',
    '14:00', '14:30',
    '15:00', '15:30',
    '16:00', '16:30',
    '17:00', '17:05', '17:10', '17:15', '17:20', '17:25', '17:30', '17:35', '17:40', '17:45', '17:50', '17:55',
    '18:00', '18:05', '18:10', '18:15', '18:20', '18:25', '18:30', '18:35', '18:40', '18:45', '18:50', '18:55',
    '19:00', '19:05', '19:10', '19:15', '19:20', '19:25', '19:30', '19:35', '19:40', '19:45', '19:50', '19:55',
    '20:00', '20:30', '20:50',
    '21:30'
    ]

# К метро Пролетарская
    toProletarskaya = [
    '08:00', '08:05', '08:10', '08:15', '08:20', '08:25', '08:30', '08:35', '08:40', '08:45', '08:50', '08:55',
    '09:00', '09:05', '09:10', '09:15', '09:20', '09:25', '09:30', '09:35', '09:40', '09:45', '09:50', '09:55',
    '10:00', '10:05', '10:10', '10:15', '10:20', '10:25', '10:30', '10:35', '10:40', '10:45', '10:50', '10:55',
    '11:00', '11:30',
    '12:00', '12:30',
    '13:00', '13:30',
    '14:00', '14:30',
    '15:00', '15:30',
    '16:00', '16:30',
    '17:00', '17:05', '17:10', '17:15', '17:20', '17:25', '17:30', '17:35', '17:40', '17:45', '17:50', '17:55',
    '18:00', '18:05', '18:10', '18:15', '18:20', '18:25', '18:30', '18:35', '18:40', '18:45', '18:50', '18:55',
    '19:00', '19:05', '19:10', '19:15', '19:20', '19:25', '19:30', '19:35', '19:40', '19:45', '19:50', '19:55',
    '20:00', '20:30',
    '21:00'
    ]

# fromIlyicha
    if weekday <= 3: # От метро (ПН-ЧТ)
        fromIlyicha = fromsub_workdays
    elif weekday == 4: # От метро (ПТ)
        fromIlyicha = fromsub_workdays[:] # create copy of list to not alter original
        fromIlyicha.remove('17:35')
    else: # print("От метро (СБ-ВС)")
        fromIlyicha = fromsub_weekends
    for i in fromIlyicha:
        if i >= time:
            nextbusfromIlyicha = i
            break

# toIlyicha
    if weekday <= 3: # К метро (ПН-ЧТ)
        toIlyicha = tosub_workdays[:]
        toIlyicha.extend(tosub_monthu)
    elif weekday == 4: # К метро (ПТ)
        toIlyicha = tosub_workdays[:]
        toIlyicha.extend(tosub_fri)
    else: # К метро (СБ-ВС)
        toIlyicha = tosub_weekends
    for i in toIlyicha:
        if i >= time:
            nextbustoIlyicha = i
            break

# fromPaveletskaya
    for i in fromPaveletskaya:
        if i >= time:
            nextbusfromPaveletskaya = i
            break
# toPaveletskaya
    for i in toPaveletskaya:
        if i >= time:
            nextbustoPaveletskaya = i
            break
# fromProletarskaya
    for i in fromProletarskaya:
        if i >= time:
            nextbusfromProletarskaya = i
            break
# toProletarskaya
    for i in toProletarskaya:
        if i >= time:
            nextbustoProletarskaya = i
            break

    if not nextbusfromIlyicha:
        fromIlyicha = "Последний автобус *от пл. Ильича* уже ушёл\n"
    else:
        fromIlyicha = "Автобус *от пл. Ильича* в *" + nextbusfromIlyicha + "*\n"
    if not nextbustoIlyicha:
        toIlyicha = "Последний автобус *к пл. Ильича* уже ушёл\n"
    else:
        toIlyicha = "Автобус *к пл. Ильича* в *" + nextbustoIlyicha + "*\n"
    if not nextbusfromPaveletskaya:
        fromPaveletskaya = "Последний автобус *от Павелецкой* уже ушёл\n"
    else:
        fromPaveletskaya = "Автобус *от Павелецкой* в *" + nextbusfromPaveletskaya + "*\n"
    if not nextbustoPaveletskaya:
        toPaveletskaya = "Последний автобус *к Павелецкой* уже ушёл\n"
    else:
        toPaveletskaya = "Автобус *к Павелецкой* в *" + nextbustoPaveletskaya + "*\n"
    if not nextbusfromProletarskaya:
        fromProletarskaya = "Последний автобус *от Пролетарской* уже ушёл\n"
    else:
        fromProletarskaya = "Автобус *от Пролетарской* в *" + nextbusfromProletarskaya + "*\n"
    if not nextbustoProletarskaya:
        toProletarskaya = "Последний автобус *к Пролетарской* уже ушёл\n"
    else:
        toProletarskaya = "Автобус *к Пролетарской* в *" + nextbustoProletarskaya + "*\n"
    sep = "-------------------------------------------\n"
    warn = "*Автобусы от и к Павелецкой временно не ходят*\n"
#    schedule = fromIlyicha + toIlyicha + sep + fromPaveletskaya + toPaveletskaya + sep + fromProletarskaya + toProletarskaya
    schedule = fromIlyicha + toIlyicha + sep + warn + sep + fromProletarskaya + toProletarskaya
    context.bot.send_message(chat_id=update.effective_chat.id, text=schedule, parse_mode='Markdown')


def smirn(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('images/bus-smirn.jpg', 'rb'))
def pavel(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('images/bus-pavel.png', 'rb'))
def prolet(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('images/bus-prolet.png', 'rb'))

def msg(update, context):
    text = 'Текущее время на сервере c PSBus: ' + str(datetime.now(pytz.timezone(os.getenv('TZ'))).time())
    context.bot.send_message(chat_id='-1001449147903', text=text, parse_mode='HTML')

def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="/bus - следующий автобус\n\
/smirn - расписание Смирновка\n\
/pavel - расписание Павелецкая\n\
/prolet - расписание Пролетарская")

# Handlers
start_handler = CommandHandler('start', start)
help_handler = CommandHandler('help', help)
bus_handler = CommandHandler('bus', bus)
smirn_handler = CommandHandler('smirn', smirn)
prolet_handler = CommandHandler('prolet', prolet)
pavel_handler = CommandHandler('pavel', pavel)
msg_handler = CommandHandler('msg', msg) # разово отправить сообщение в нужный чат

dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(bus_handler)
dispatcher.add_handler(smirn_handler)
dispatcher.add_handler(prolet_handler)
dispatcher.add_handler(pavel_handler)
dispatcher.add_handler(msg_handler)

# Webhook for Heroku
PORT = int(os.environ.get('PORT', 5000))
updater.start_webhook(listen="0.0.0.0", port=int(PORT), url_path=telegram_token)
updater.bot.setWebhook(heroku_url + telegram_token)

updater.idle()
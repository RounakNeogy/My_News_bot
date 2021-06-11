import logging
from flask import Flask,request
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters,Dispatcher
from telegram import Bot,Update,ReplyKeyboardMarkup
from utils import fetch_news, get_reply,topics_keyboard
#enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
                    level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN="1806533440:AAFMAoAB4Snpvcs78NYSIJSaP7zsZUXn4X4"

app=Flask(__name__)

@app.route('/')
def index():
    return "Hello!"

# Create view to handle webhooks
@app.route(f'/{TOKEN}', methods=['GET', 'POST'])
def webhook():
    """webhook view which receives updates from telegram"""
    # create update object from json-format request data
    update = Update.de_json(request.get_json(), bot)
    # process update
    dp.process_update(update)
    return "ok"

def start(update, context):
    print(update)
    author=update.message.from_user.first_name
    reply=f"Hey!! {author}"
    context.bot.send_message(chat_id=update.effective_chat.id,text=reply)

def _help(update, context):
    reply="This is a help text"
    context.bot.send_message(chat_id=update.effective_chat.id,text=reply)

def news(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Choose a category", 
        reply_markup=ReplyKeyboardMarkup(keyboard=topics_keyboard, one_time_keyboard=True))

def reply_text(update, context):
    intent,reply= get_reply(update.message.text,update.effective_chat.id)
    if intent=="get_news":
        articles=fetch_news(reply)
        for article in articles:
            context.bot.send_message(chat_id=update.effective_chat.id,text=article['link'])
    else:
        context.bot.send_message(chat_id=update.effective_chat.id,text=reply)

def echo_sticker(update, context):
    reply=update.message.sticker.file_id
    context.bot.send_sticker(chat_id=update.effective_chat.id,sticker=reply)

def error(bot,update):
    logger.error("Update '%s' caused error '%s'",update, update.error)

# create telegram bot object
bot=Bot(TOKEN)
# set webhook for telegram bot
try: 
    bot.set_webhook("https://desolate-fortress-59481.herokuapp.com/" + TOKEN)
except Exception as e:
    print(e)
# Create Dispatcher
dp = Dispatcher(bot,None)
# Add handlers
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("help", _help))
dp.add_handler(CommandHandler("news", news))
dp.add_handler(MessageHandler(Filters.text, reply_text))
dp.add_handler(MessageHandler(Filters.sticker, echo_sticker))
dp.add_error_handler(error)
# main function      
if __name__=='__main__':
    app.run(port=8443)
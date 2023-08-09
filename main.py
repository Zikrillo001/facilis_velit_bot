from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, ConversationHandler
from database import Database
from messages import message_handler
from locations import location_handler
from inlines import inline_handler
from register import check_user

TOKEN = "6327938286:AAEKNU4aMAXAju3KSFAC_c4om9FBdKGypVc"
ADMIN_ID = 986596808
db = Database("farmacy.db")


def start_handler(update, context):
    # print(context.user_data.get("my_name_is", 0))
    # context.user_data["my_name_is"] = "eminem"
    check_user(update, context)


def contact_handler(update, context):
    pass


def main():
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start_handler))
    dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
    dispatcher.add_handler(MessageHandler(Filters.contact, contact_handler))
    dispatcher.add_handler(CallbackQueryHandler(inline_handler))
    dispatcher.add_handler(MessageHandler(Filters.location, location_handler))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

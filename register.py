from telegram import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from database import Database
from messages import main_menu
import globals

db = Database("farmacy.db")


def check_user(update, context):
    user = update.message.from_user
    # print(user)
    # lang_id = context.user_data.get("lang_id", None)
    db_user = db.get_user_by_chat_id(user.id)
    print(db_user)

    if not db_user:
        db.create_user(user)
        update.message.reply_text(text=globals.WELCOME_TEXT)
        db_user = db.get_user_by_chat_id(user.id)
    if not db_user["lang_id"]:
        buttons = [
            [KeyboardButton(text=globals.BTN_LANG_UZ), KeyboardButton(text=globals.BTN_LANG_RU),
             KeyboardButton(text=globals.BTN_LANG_ENG)]
        ]
        update.message.reply_text(
            text=globals.CHOOSE_LANG,
            reply_markup=ReplyKeyboardMarkup(
                keyboard=buttons,
                resize_keyboard=True
            )
        )
    else:
        main_menu(update, context)
        # context.user_data["state"] = globals.STATES["reg"]

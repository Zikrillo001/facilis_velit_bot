from database import Database
from telegram import KeyboardButton, ReplyKeyboardMarkup
import globals

db = Database("farmacy.db")


def message_handler(update, context):
    """
    messagelarni ushlaydi
    :param update:
    :param context:
    :return:
    """
    message = update.message.text
    # print(message)
    user = update.message.from_user
    db_user = db.get_user_by_chat_id(user.id)
    if context.user_data.get("lang_id", False):
        context.user_data["lang_id"] = db_user["lang_id"]
    if message in ["🇺🇿 UZ", "🇷🇺 RU", "🏴󠁧󠁢󠁥󠁮󠁧󠁿󠁧󠁢󠁥󠁮 ENG"]:
        get_lang(update, context)
    elif not db_user["lang_id"]:
        send_request_lang(update, context)
    elif message in globals.MAIN_MEMU_LISTS:
        main_menu_handler(update, context)
    elif message in globals.GO_MAIN_MENU:
        main_menu(update, context)
    elif message in globals.ALL_INFO_RESULT:
        pass
        #### boshqa shartlar.


    elif isinstance(message, str):
        search_drug(update, context)
    # main_menu(update, context)


def send_request_lang(update, context):
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


def get_lang(update, context):
    message = update.message.text
    # print(message)
    user = update.message.from_user
    db_user = db.get_user_by_chat_id(user.id)
    if message == "🇺🇿 UZ":
        context.user_data["lang_id"] = 1
    elif message == "🇷🇺 RU":
        context.user_data["lang_id"] = 2
    elif message == "🏴󠁧󠁢󠁥󠁮󠁧󠁿󠁧󠁢󠁥󠁮 ENG":
        context.user_data["lang_id"] = 3
    else:
        context.user_data["lang_id"] = db_user["lang_id"]
    db.update_user_data(chat_id=user.id, key="lang_id", value=context.user_data["lang_id"])
    main_menu(update, context)


def main_menu(update, context):
    message = update.message.text
    user = update.message.from_user
    lang_id = int(context.user_data.get("lang_id", db.get_user_by_chat_id(user.id)["lang_id"]))
    # print(lang_id)
    buttons = [
        [KeyboardButton(text=globals.SEARCH_BUTTON_TEXT[lang_id - 1])],
        [KeyboardButton(text=globals.INFORMATION_BUTTON_TEXT[lang_id - 1]),
         KeyboardButton(text=globals.HELP_ADVICE_BUTTON_TEXT[lang_id - 1])],
        [KeyboardButton(text=globals.COMMENT_BUTTON_TEXT[lang_id - 1]),
         KeyboardButton(text=globals.CHANGE_LANG_BUTTON_TEXT[lang_id - 1])],
        [KeyboardButton(text=globals.ABOUT_US_BUTTON_TEXT[lang_id - 1])]

    ]
    update.message.reply_text(
        text=globals.CHOOSE_MENU[lang_id - 1],
        reply_markup=ReplyKeyboardMarkup(
            keyboard=buttons,
            resize_keyboard=True
        )
    )


def main_menu_handler(update, context):
    message = update.message.text
    user = update.message.from_user
    db_user = db.get_user_by_chat_id(user.id)
    if message in globals.SEARCH_BUTTON_TEXT:
        update.message.reply_text(text=globals.SEARCH_BUTTON_RESULT[int(db_user["lang_id"]) - 1])
    elif message in globals.INFORMATION_BUTTON_TEXT:
        send_information_menu(update, context, db_user)
    elif message in globals.HELP_ADVICE_BUTTON_TEXT:
        for_connect_doctors(update, context, db_user)
    elif message in globals.COMMENT_BUTTON_TEXT:
        comment_us(update, context, db_user)
    elif message in globals.CHANGE_LANG_BUTTON_TEXT:
        send_lang_options(update, message, db_user)
    elif message in globals.ABOUT_US_BUTTON_TEXT:
        about_us(update, context, db_user)
        # search_drug(update, context)


def search_drug(update, context):
    message = update.message.text
    user = update.message.from_user
    db_user = db.get_user_by_chat_id(user.id)
    # cyrillic_text = "Привет, мир!"

    lang_id = int(context.user_data.get("lang_id", db.get_user_by_chat_id(update.message.from_user.id)["lang_id"]))
    if len(message) < 3:
        # print(message)
        update.message.reply_text(text=globals.DRUG_RESTRICTION[lang_id - 1])

    else:
        db_drugs = db.search_drugs_by_text(message[:3])
        buttons = [[KeyboardButton(text=globals.GO_MAIN_MENU[int(db_user["lang_id"]) - 1])]]
        for i in db_drugs:
            buttons.append([KeyboardButton(text=i["name"])])
        update.message.reply_text(
            text=globals.SEARCH_BUTTON_RESULT[int(db_user["lang_id"]) - 1],
            reply_markup=ReplyKeyboardMarkup(
                keyboard=buttons,
                resize_keyboard=True
            )
        )


def send_lang_options(update, context, db_user):
    buttons = [
        [KeyboardButton(text=globals.BTN_LANG_UZ), KeyboardButton(text=globals.BTN_LANG_RU),
         KeyboardButton(text=globals.BTN_LANG_ENG)],
        [KeyboardButton(text=globals.GO_MAIN_MENU[int(db_user["lang_id"]) - 1])]
    ]
    update.message.reply_text(
        text=globals.CHOOSE_LANG,
        reply_markup=ReplyKeyboardMarkup(
            keyboard=buttons,
            resize_keyboard=True
        )
    )


def send_information_menu(update, context, db_user):
    buttons = [
        [KeyboardButton(text=globals.INFO_BUTTON_RESULT_DRUG[int(db_user["lang_id"]) - 1])],
        [KeyboardButton(text=globals.INFO_BUTTON_RESULT_DISEASES[int(db_user["lang_id"]) - 1])],
        [KeyboardButton(text=globals.GO_MAIN_MENU[int(db_user["lang_id"]) - 1])]
    ]
    update.message.reply_text(
        text=globals.INFORMATION_BUTTON_TEXT[int(db_user["lang_id"]) - 1],
        reply_markup=ReplyKeyboardMarkup(
            keyboard=buttons,
            resize_keyboard=True
        )
    )


def for_connect_doctors(update, context, db_user):
    update.message.reply_text(text=globals.TEXNICAL_WORK_DOCTORS[int(db_user["lang_id"]) - 1])


def comment_us(update, context, db_user):
    update.message.reply_text(text=globals.COMMENT_BUTTON_RESULT[int(db_user["lang_id"]) - 1])


def about_us(update, context, db_user):
    update.message.reply_text(text=globals.ABOUT_US[int(db_user["lang_id"]) - 1])

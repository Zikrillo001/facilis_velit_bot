from telegram import Bot

WELCOME_TEXT = (f"Assalomu aleykum xush kelibsiz bu Dori top bot\n"
                f"Hello and welcome this is Dori top bot\n"
                f"Привет и добро пожаловать, это бот Dori Top\n")
# print(Bot.username.__str__())
CHOOSE_LANG = "Tilni tanlang / Выберите язык / Choose language!"
BTN_LANG_UZ = "🇺🇿 UZ"
BTN_LANG_RU = "🇷🇺 RU"
BTN_LANG_ENG = "🏴󠁧󠁢󠁥󠁮󠁧󠁿󠁧󠁢󠁥󠁮 ENG"
STATES = {
    "reg": 1,
    "menu": 2,
    "settings": 3
}

CHOOSE_MENU = [
    "📲👇 Kerakli bo'limni tanlang yoki 💊 dori nomini kiriting.",
    "📲👇 Выберите нужный раздел или введите название 💊 препарата.",
    "📲👇 Select the desired section or enter the name of 💊 medicine."
]

SEARCH_BUTTON_TEXT = [
    "🔍 Qidirish.",
    "🔍 Поиск.",
    "🔍 Search.",
]

INFORMATION_BUTTON_TEXT = [
    "ℹ️ Malumot olish.",
    "️️ℹ️  ️Получить информацию.",
    "️ℹ️  ️Get information.",
]
HELP_ADVICE_BUTTON_TEXT = [
    "🥼 Shifokor maslahati.",
    "️️🥼 Совет врача.",
    "️🥼 Doctor's advice.",
]
COMMENT_BUTTON_TEXT = [
    "💬 Fikr bildirish.",
    "️️💬 Комментарий.",
    "️💬 Comment.",
]

CHANGE_LANG_BUTTON_TEXT = [
    "🔄 Tilni o'zgartirish.",
    "️️🔄 Изменить язык.",
    "️🔄 Change language.",
]
ABOUT_US_BUTTON_TEXT = [
    "Biz haqimizda ⁉️",
    "️О нас ⁉️",
    "️About us ⁉️",
]

GO_MAIN_MENU = [
    "🏠 Bosh sahifa",
    "🏠 Домашняя страница",
    "🏠 Home page"
]

MAIN_MEMU_LISTS = (SEARCH_BUTTON_TEXT + INFORMATION_BUTTON_TEXT +
                   HELP_ADVICE_BUTTON_TEXT + CHANGE_LANG_BUTTON_TEXT +
                   ABOUT_US_BUTTON_TEXT + COMMENT_BUTTON_TEXT)
# print(MAIN_MEMU_LISTS)
DRUG_RESTRICTION = [
    "❗️Ushbu qidiruv bo'yicha dorilar topilmadi. 💊 Dori nomini kiriting (kamida 3 belgi yozing)",
    "️❗️Никаких препаратов по данному запросу не найдено. 💊 Введите название лекарства (напишите не менее 3 символов)",
    "️❗️No drugs were found for this search. 💊 Enter the name of the medicine (write at least 3 characters)",
]
SEARCH_BUTTON_RESULT = [
    "💊 Dori nomini kiriting (kamida 3 belgi yozing)",
    "💊 Введите название лекарства (напишите не менее 3 символов)",
    "💊 Enter the name of the medicine (write at least 3 characters)",
]
COMMENT_BUTTON_RESULT = [
    "Hurmatli foydalanuvchi, agar sizda shiloyat,taklif va mulohazalar bo'lsa bizning adminimiz bilan bog'lanishingiz mumkin. \n admin-username: @diyorbekbakhshullayev\ntel1: +998 93 082 09 30\ntel2: +998 91 083 09 30",
    "Уважаемый пользователь, если у вас есть жалобы, предложения и замечания, вы можете обратиться к нашему администратору. \n имя пользователя-администратора: @diyorbekbakhshullayev\ntel1: +998 93 082 09 30\ntel2: +998 91 083 09 30",
    "Dear user, if you have any complaints, suggestions and comments, you can contact our admin. \n admin-username: @diyorbekbakhshullayev\ntel1: +998 93 082 09 30\ntel2: +998 91 083 09 30",
]
INFO_BUTTON_RESULT_TEXT = [
    "❔ Nima haqida malumot olmoqchisiz?",
    "❔ О чем вы хотите узнать?",
    "❔ What do you want to know about?"
]
INFO_BUTTON_RESULT_DRUG = [
    "💊 Dorilar haqida malumot",
    "💊 Информация о лекарствах",
    "💊 Information about medicines"
]
INFO_BUTTON_RESULT_DISEASES = [
    "🦠 Kasalliklar haqida malumot",
    "🦠 Информация о заболеваниях",
    "🦠 Information about diseases",
]
ALL_INFO_RESULT = INFO_BUTTON_RESULT_DISEASES + INFO_BUTTON_RESULT_DRUG

TEXNICAL_WORK_DOCTORS = [
    "Kechirasiz dasturimizni bu qismi bo'yicha hali tehxnik 🛠 ko'riklar olib borilmoqda.",
    "К сожалению, эта часть нашей программы все еще находится на технической 🛠 проверке.",
    "Sorry, this part of our program is still under technical 🛠 review.",
]
ABOUT_US = [
    "Bu botimiz 🤖 sizga dorilarni 💊 tez va oson topish, ular haqida sifatli malumot ℹ️ olishga qaratilgan\n\nKeyingi versiyalarda shifokor 👨🏼‍⚕️ maslahatini ham qo'shish niyatimiz bor.\nBiz bilan qoling",
    "Наш бот 🤖 призван помочь вам быстро и легко найти лекарства 💊 и получить качественную информацию ℹ️ о них\n\nВ следующих версиях мы намерены добавить консультацию врача 👨🏼‍⚕️.\nОставайтесь с нами",
    "Our bot 🤖 is aimed at helping you find medicines 💊 quickly and easily, and get quality information ℹ️ about them\n\nIn the next versions, we intend to add doctor's advice 👨🏼‍⚕️.\nStay with us️"
]

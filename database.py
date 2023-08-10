import sqlite3


class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.cur = self.conn.cursor()

    def create_user(self, user):
        print(user)
        self.cur.execute("""insert into user (first_name, username, chat_id) values (?, ?, ?)""",
                         (user["first_name"], user["username"], user["id"],))
        self.conn.commit()

    def update_user_data(self, chat_id, key, value):
        self.cur.execute(f"""update user set {key} = ? where chat_id = ?""", (value, chat_id))
        self.conn.commit()

    def get_user_by_chat_id(self, chat_id):
        self.cur.execute("""select * from user where chat_id = ?""", (chat_id,))
        user = dict_fetchone(self.cur)
        return user

    def search_drugs_by_text(self, name_text):
        self.cur.execute("""SELECT * FROM drugs WHERE SUBSTR(name, 1, 3) = ?""", (name_text,))

        drugs = dict_fetchall(self.cur)
        print(drugs)
        return drugs


def dict_fetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def dict_fetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))

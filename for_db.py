from data import db_session


class BotDB:
    def __int__(self):
        db_session.global_init("db/user_data.db")

db = BotDB()
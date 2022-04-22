from data import db_session
from data.users import User


class BotDB:
    def __init__(self):
        db_session.global_init("db/user_data.db")

    def check(self):


    def add_us(self, id_u):
        user = User()
        user.user_id = id_u
        db_sess = db_session.create_session()
        db_sess.add(user)
        db_sess.commit()


bot_db = BotDB()
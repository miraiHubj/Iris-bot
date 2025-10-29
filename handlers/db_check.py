import sqlite3
import datetime

class CheckDB():
    
    def __init__(self):
        self.db = sqlite3.connect('chapcha_data_base.db')
        self.c = self.db.cursor()
        self.db.commit()
        self.db.close()
    
    def add_user(self, message):
        self.date_pre = datetime.datetime.now()
        self.date_time = self.date_pre.strftime("%Y-%m-%d %H:%M:%S")
        self.db = sqlite3.connect('chapcha_data_base.db')
        self.c = self.db.cursor()
        self.date_now = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        self.date_now = datetime.datetime.strptime(self.date_now, '%Y-%m-%d %H:%M:%S')
        self.date_change = datetime.timedelta(days=1)
        self.date_new = self.date_now - self.date_change
        self.c.execute("INSERT INTO user_data VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (message.from_user.id, message.from_user.username, message.from_user.first_name, 'НоуНейм', message.from_user.first_name, 0, str(self.date_time), 'Безработный', 0, 0, 0, 0, 0, 0, str(self.date_new), 'YES', 'YES', 'YES'))
        self.c.execute("INSERT INTO nicks_auction VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (message.from_user.id, message.from_user.first_name, '', '', '', '', '', '', '', ''))
        self.c.execute("INSERT INTO game_clicker VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (message.from_user.id, 1, 1, 2000, 1, 1, 20000))
        self.c.execute("INSERT INTO game_farm VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (message.from_user.id, 1, 100, 2000, 1, 5, 100000))
        self.c.execute("INSERT INTO game_cube VALUES (?, ?, ?, ?)",
                   (message.from_user.id, 1, 2, 25000))
        self.c.execute("INSERT INTO game_slot_machine VALUES (?, ?, ?, ?)",
                   (message.from_user.id, 1, 10, 15000))
        self.c.execute("INSERT INTO game_darts VALUES (?, ?, ?, ?)",
                   (message.from_user.id, 1, 2, 25000))
        self.c.execute("INSERT INTO game_stealing VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (message.from_user.id, 1, 10, 20000, 1, 1, 20000, 1, 1, 2000))
        self.c.execute(f"INSERT INTO game_case VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (message.from_user.id, str(self.date_new), 1, 10, 20000, 1, 0.5, 100000, 0, 0, 0, 0, 0))
        self.c.execute("INSERT INTO purchases VALUES (?, ?, ?, ?, ?, ?)",
                   (message.from_user.id, 0, 0, 0, 0, 0))
        self.db.commit()
        self.db.close()
    
    def update(self, message):
        self.db = sqlite3.connect('chapcha_data_base.db')
        self.c = self.db.cursor()
        self.c.execute(f"""UPDATE user_data SET
user_username = '{message.from_user.username}',
user_name = '{message.from_user.first_name}'
WHERE user_id = {message.from_user.id}""")
        self.db.commit()
        self.db.close()
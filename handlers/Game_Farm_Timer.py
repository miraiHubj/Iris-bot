import sqlite3
import asyncio

class Game_Farm_Timer():
    async def wait_for_farm(self, ui, ulf):
        while ulf > 0:
            await asyncio.sleep(1)
            update_ulf = ulf - 1
            ulf = update_ulf
            print(ulf)
            db = sqlite3.connect('chapcha_data_base.db')
            c = db.cursor()
            c.execute(f"UPDATE user_data SET user_last_farm = {update_ulf} WHERE user_id = {ui}")
            db.commit()
            db.close()
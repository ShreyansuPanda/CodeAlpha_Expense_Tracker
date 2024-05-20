import sqlite3
class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS expense_record (item_name text, item_price float, purchase_date date)")
        self.conn.commit()

    def fetchrecord(self, query):
        self.cur.execute(query)
        rows = self.cur.fetchall()
        return rows

    def insertrecords(self, item_name, item_price, purchase_date):
        self.cur.execute("INSERT INTO expense_record VALUES (?, ?, ?)", (item_name, item_price, purchase_date))
        self.conn.commit()

    def removerecord(self, rwid):
        rwid_int = int(rwid)
        self.cur.execute("DELETE FROM expense_record WHERE rowid=?", (rwid_int,))
        self.conn.commit()

    def updaterecord(self, item_name, item_price, purchase_date, rid):
        self.cur.execute("UPDATE expense_record SET item_name = ?, item_price = ?, purchase_date = ? WHERE rowid = ?",
                         (item_name, item_price, purchase_date, rid))
        self.conn.commit()

    def delete_all_records(self):
        self.cur.execute("DELETE FROM expense_record")
        self.conn.commit()

    def __del__(self):
        self.conn.close()

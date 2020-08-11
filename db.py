import mysql.connector


class Database:
    def __init__(self, db):
        self.conn = mysql.connector.connect(
            host=db['host'],
            user=db['user'],
            password=db['password'],
            database=db['database']
        )
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS parts ("
                         "id INTEGER PRIMARY KEY,"
                         "part text,"
                         "customer text,"
                         "retailer text,"
                         "price text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM parts")
        rows = self.cur.fetchall()
        return rows

    def insert(self, part, customer, retailer, price):
        self.cur.execute("INSERT INTO parts VALUES (NULL, %s, %s, %s, %s)", (part, customer, retailer, price))
        self.conn.commit()

    def remove(self, _id):
        self.cur.execute("DELETE FROM parts WHERE id = %s", (_id,))
        self.conn.commit()

    def update(self, _id, part, customer, retailer, price):
        self.cur.execute("UPDATE parts SET part = %s, customer = %s, retailer = %s, price = %s WHERE id = %s", (part, customer, retailer, price, _id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


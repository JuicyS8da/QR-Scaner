import sqlite3
import datetime

connection = sqlite3.connect('spendings-sqlite.db')

cursor = connection.cursor()

def start_db():
    cursor.execute('''CREATE TABLE IF NOT EXISTS spending
    (operation_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT,
    price INT, quantity INT, sum INT, date DATE)
    ''')

def insert_qr_data(query_dict_lenta):
    items_list = query_dict_lenta['ticket']['document']['receipt']['items']
    items_tuple = list()
    date = query_dict_lenta['process'][0]['time'][0:-6]
    date = str(datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S"))

    for i in items_list:
        item = (i['name'], i['price'], i['quantity'], i['sum'], date)
        items_tuple.append(item)

    cursor.executemany('''
                        INSERT INTO spending(name, price, quantity, sum, date)
                        VALUES (?,?,?,?,?)
    ''', items_tuple)

def drop_db():
    cursor.execute(f"""DROP TABLE spending""")

def show_db():
    cursor.execute('SELECT * FROM spending')
    print(cursor.fetchall())




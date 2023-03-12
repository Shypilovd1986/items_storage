import mysql.connector as mod


conn = mod.connect(
    host="localhost",
    user="root",
    passwd="19865421",
)

my_cursor = conn.cursor()

my_cursor.execute("CREATE DATABASE IF NOT EXISTS items_storage")

my_cursor.execute("SHOW DATABASES")

for db in my_cursor:
    print(db)

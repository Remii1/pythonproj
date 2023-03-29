import sqlite3

conn = sqlite3.connect('companh.db')
print("Successfully opened database")

conn.execute("""CREATE TABLE Company1(
ID INT PRIMARY KEY NOT NULL,
FIRSTNAME TEXT NOT NULL,
LASTNAME TEXT NOT NULL,
AGE INT,
SALARY REAL,
TASK TEXT CHAR(20))""")

print("Successfully created Company1table")
conn.close()

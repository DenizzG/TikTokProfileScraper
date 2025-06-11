import sqlite3

db_name = input("Enter database filename (e.g., fitness.db): ")
table_name = input("Enter table name (e.g., profiles): ")

conn = sqlite3.connect(db_name)
cur = conn.cursor()

# Show columns
cur.execute(f"PRAGMA table_info({table_name});")
columns = [col[1] for col in cur.fetchall()]
print("Columns:", columns)

# Show first 10 rows
cur.execute(f"SELECT * FROM {table_name};")
rows = cur.fetchall()
for row in rows:
    print(row)

conn.close()
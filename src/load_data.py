import csv
import sqlite3

CSV_PATH = "data/clean/clean_data.csv"
DB_PATH = "crypto.db"

print("📥 بدء تحميل البيانات إلى SQLite...")

# 1. فتح الاتصال بقاعدة البيانات
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# 2. قراءة CSV النظيف
with open(CSV_PATH, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

# 3. إدراج كل صف
inserted = 0
for row in rows:
    # INSERT OR REPLACE: إذا العملة موجودة، يتم تحديثها. وإلا تُدرج جديدة.
    cursor.execute("""
        INSERT OR REPLACE INTO prices (coin, price_usd, change_24h, fetch_time)
        VALUES (?, ?, ?, ?)
    """, (
        row["coin"],
        row["price_usd"],
        row["change_24h"],
        row["fetch_time"]
    ))
    inserted += 1

# 4. حفظ التغييرات
conn.commit()
conn.close()

print(f"✅ تم تحميل {inserted} صفًا إلى جدول prices.")

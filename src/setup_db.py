import sqlite3
import os

DB_PATH = "crypto.db"

# حذف قاعدة البيانات القديمة إن وُجدت (للتنظيف أثناء التطوير)
if os.path.exists(DB_PATH):
    os.remove(DB_PATH)
    print("🗑️  حذف قاعدة البيانات القديمة لإعادة البناء.")

# إنشاء اتصال جديد
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# إنشاء جدول الأسعار
cursor.execute("""
    CREATE TABLE IF NOT EXISTS prices (
        coin TEXT PRIMARY KEY,
        price_usd REAL,
        change_24h REAL,
        fetch_time TEXT
    )
""")

# تأكيد وحفظ
conn.commit()
conn.close()

print(f"✅ تم إنشاء قاعدة البيانات '{DB_PATH}' وجدول 'prices' بنجاح.")

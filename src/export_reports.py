import csv
import os
import sqlite3

DB_PATH = "crypto.db"
REPORTS_DIR = "data/reports"

# تأكد من وجود مجلد التقارير
os.makedirs(REPORTS_DIR, exist_ok=True)

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# 1. تقرير: أعلى سعر لكل عملة
cursor.execute("SELECT coin, MAX(price_usd) as max_price FROM prices GROUP BY coin")
with open(f"{REPORTS_DIR}/max_prices.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["coin", "max_price_usd"])
    writer.writerows(cursor.fetchall())

# 2. تقرير: الترتيب الحالي
cursor.execute("SELECT coin, price_usd FROM prices ORDER BY price_usd DESC")
with open(f"{REPORTS_DIR}/current_ranking.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["coin", "price_usd"])
    writer.writerows(cursor.fetchall())

# 3. تقرير: ملخص التغير
cursor.execute("SELECT AVG(change_24h), MIN(change_24h), MAX(change_24h) FROM prices")
avg, min_c, max_c = cursor.fetchone()
with open(f"{REPORTS_DIR}/change_summary.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["metric", "value"])
    writer.writerows([
        ["avg_change_24h", avg],
        ["min_change_24h", min_c],
        ["max_change_24h", max_c]
    ])

conn.close()

print("✅ تم تصدير التقارير إلى:")
print(f"   📁 {REPORTS_DIR}/")
for fname in os.listdir(REPORTS_DIR):
    print(f"   📄 {fname}")

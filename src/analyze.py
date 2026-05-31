import sqlite3

DB_PATH = "crypto.db"

print("📊 بدء التحليل...\n")

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# 1. أعلى سعر لكل عملة
print("1. أعلى سعر لكل عملة (من البيانات المسجلة):")
cursor.execute("SELECT coin, MAX(price_usd) FROM prices GROUP BY coin")
for row in cursor.fetchall():
    print(f"   {row[0]}: ${row[1]:,.2f}" if row[1] else f"   {row[0]}: لا توجد بيانات")

# 2. ترتيب العملات من الأعلى سعرًا إلى الأقل
print("\n2. ترتيب العملات حسب السعر الحالي:")
cursor.execute("SELECT coin, price_usd FROM prices ORDER BY price_usd DESC")
for row in cursor.fetchall():
    print(f"   {row[0]}: ${row[1]:,.2f}" if row[1] else f"   {row[0]}: لا توجد بيانات")

# 3. متوسط التغير في 24 ساعة
print("\n3. متوسط التغير في 24 ساعة:")
cursor.execute("SELECT AVG(change_24h) FROM prices")
avg_change = cursor.fetchone()[0]
if avg_change:
    print(f"   المتوسط: {avg_change:.2f}%")
else:
    print("   لا توجد بيانات كافية.")

conn.close()
print("\n✅ انتهى التحليل.")

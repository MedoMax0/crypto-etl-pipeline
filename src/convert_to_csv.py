import json
import csv
import os

# 1. قراءة ملف JSON الخام
with open("data/raw/raw_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 2. استخراج وقت الجلب
fetch_time = data.get("fetch_time", "Unknown")

# 3. تجهيز صفوف CSV
rows = []
for coin_name, coin_info in data.items():
    # نتخطى المفاتيح غير العملات (مثل fetch_time)
    if coin_name == "fetch_time":
        continue
    
    # نستخرج البيانات بأمان (إذا لم يوجد حقل، نضع None)
    price = coin_info.get("usd")
    change = coin_info.get("usd_24h_change")
    
    rows.append({
        "coin": coin_name,
        "price_usd": price,
        "change_24h": change,
        "fetch_time": fetch_time
    })

# 4. حفظ CSV
os.makedirs("data/raw", exist_ok=True)
file_path = "data/raw/raw_data.csv"
with open(file_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["coin", "price_usd", "change_24h", "fetch_time"])
    writer.writeheader()
    writer.writerows(rows)

print(f"✅ تم تحويل JSON إلى CSV: {file_path}")
print(f"📊 عدد العملات: {len(rows)}")

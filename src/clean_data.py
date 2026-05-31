import csv
import os
from datetime import datetime

RAW_PATH = "data/raw/raw_data.csv"
CLEAN_PATH = "data/clean/clean_data.csv"

print("🧹 بدء تنظيف البيانات...")

# قراءة البيانات الخام
with open(RAW_PATH, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

cleaned_rows = []
seen_coins = set()

for row in rows:
    coin = row.get("coin", "").strip()
    price_str = row.get("price_usd", "").strip()
    change_str = row.get("change_24h", "").strip()
    time_str = row.get("fetch_time", "").strip()

    # 1. تجاهل صفوف مكررة لنفس العملة (نأخذ الأول فقط)
    if coin in seen_coins:
        continue
    seen_coins.add(coin)

    # 2. تحويل النصوص إلى أرقام (مع أمان)
    try:
        price = float(price_str) if price_str else None
    except ValueError:
        price = None

    try:
        change = float(change_str) if change_str else None
    except ValueError:
        change = None

    # 3. تبسيط وقت الجلب (نأخذ الجزء YYYY-MM-DD HH:MM فقط)
    clean_time = ""
    try:
        # الصيغة الأصلية: "2026-05-29T15:15:23.855661Z"
        dt = datetime.fromisoformat(time_str.replace("Z", "+00:00"))
        clean_time = dt.strftime("%Y-%m-%d %H:%M")
    except:
        clean_time = time_str  # إذا فشل، نتركه كما هو

    cleaned_rows.append({
        "coin": coin,
        "price_usd": price,
        "change_24h": change,
        "fetch_time": clean_time
    })

# 4. كتابة CSV النظيف
os.makedirs("data/clean", exist_ok=True)
with open(CLEAN_PATH, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["coin", "price_usd", "change_24h", "fetch_time"])
    writer.writeheader()
    writer.writerows(cleaned_rows)

print(f"✅ تم التنظيف: {len(cleaned_rows)} عملة محفوظة في {CLEAN_PATH}")

# 5. ملاحظات إضافية
if len(cleaned_rows) < 5:
    print("⚠️ تنبيه: عدد العملات أقل من 5. ربما هناك عملة مفقودة من البيانات الخام.")

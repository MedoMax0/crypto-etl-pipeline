import csv

file_path = "data/raw/raw_data.csv"

print("🔍 تحليل البيانات الخام:")
print("-" * 30)

with open(file_path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

print(f"عدد الصفوف: {len(rows)}")
print(f"الأعمدة: {reader.fieldnames}")

# فحص أول 3 صفوف
print("\n📋 أول 3 صفوف:")
for i, row in enumerate(rows[:3]):
    print(f"  صف {i}: {row}")

# فحص القيم الفارغة
print("\n🕳️ القيم الفارغة (مبدئيًا):")
for col in reader.fieldnames:
    empty_count = sum(1 for row in rows if row.get(col, "").strip() == "")
    print(f"  {col}: {empty_count} خلية فارغة")

# فحص القيم غير الرقمية (مثل التواريخ أو النصوص في price)
print("\n⚠️ فحص نوع البيانات (أول 5 قيم من price_usd):")
for row in rows[:5]:
    val = row.get("price_usd", "")
    print(f"  القيمة: {val} | النوع: {type(val).__name__}")

print("\n✅ انتهى الاستكشاف. اطلع على هذه المشكلات وفكر كيف سننظفها.")

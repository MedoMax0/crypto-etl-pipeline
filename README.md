# 🚀 Crypto ETL Pipeline

مشروع **Data Engineering** كامل (End-to-End) مبني بلغة Python. يقوم بجمع بيانات أسعار العملات الرقمية من API مباشر، تنظيفها، تخزينها في قاعدة بيانات SQLite، ثم تحليلها وتصدير تقارير.

> ⚡ **رسالة للمُقيّم:** هذا المشروع وُلد وتطوّر بالكامل على هاتف Android باستخدام Termux، لإثبات أن المهارة لا تعتمد على الجهاز.

---

## 🧱 بنية المشروع

crypto-etl-pipeline/
├── data/
│   ├── raw/            # بيانات خام من API (JSON + CSV)
│   ├── clean/          # بيانات بعد التنظيف
│   └── reports/        # تقارير تحليلية جاهزة
├── src/
│   ├── fetch_data.py     # 1. جمع البيانات
│   ├── convert_to_csv.py # 2. تحويل JSON → CSV
│   ├── clean_data.py     # 3. تنظيف البيانات
│   ├── setup_db.py       # 4. إنشاء قاعدة البيانات
│   ├── load_data.py      # 5. تحميل البيانات إلى SQL
│   ├── analyze.py        # 6. استعلامات تحليلية
│   ├── export_reports.py # 7. تصدير التقارير
│   └── main.py           # 8. تشغيل الـ Pipeline كاملاً
├── crypto.db           # قاعدة بيانات SQLite
├── requirements.txt
└── README.md

---

## 🛠️ التقنيات المستخدمة

- **Python 3**: لغة البرمجة الأساسية
- **Requests**: جلب البيانات من CoinGecko API
- **JSON & CSV**: معالجة الملفات
- **SQLite3**: قاعدة بيانات علائقية
- **Git & GitHub**: إدارة النسخ
- **Termux (Android)**: بيئة التطوير والإنتاج

---

## ⚙️ كيفية التشغيل

1. **تثبيت المتطلبات:**
   ```bash
   pip install requests

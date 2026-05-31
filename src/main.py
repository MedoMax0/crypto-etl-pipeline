import subprocess
import sys
from datetime import datetime

def run_stage(script_name):
    print(f"\n{'='*40}")
    print(f"⏳ بدء: {script_name}  ({datetime.now().strftime('%H:%M:%S')})")
    result = subprocess.run([sys.executable, script_name], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"✅ نجح: {script_name}")
        print(result.stdout.strip())
    else:
        print(f"❌ فشل: {script_name}")
        print(result.stderr.strip())
        raise SystemExit(1)

if __name__ == "__main__":
    print("🚀 بدء تشغيل Crypto ETL Pipeline")
    print(f"🕒 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    stages = [
        "src/fetch_data.py",
        "src/convert_to_csv.py",
        "src/clean_data.py",
        "src/setup_db.py",
        "src/load_data.py",
        "src/analyze.py",
        "src/export_reports.py"
    ]
    
    for stage in stages:
        run_stage(stage)
    
    print(f"\n🎉 انتهى الـ Pipeline بنجاح  ({datetime.now().strftime('%H:%M:%S')})")

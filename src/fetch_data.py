import requests
import json
import os
from datetime import datetime

URL = "https://api.coingecko.com/api/v3/simple/price"
PARAMS = {
    "ids": "bitcoin,ethereum,solana,cardano,polygon",
    "vs_currencies": "usd",
    "include_24hr_change": "true"
}

response = requests.get(URL, params=PARAMS)
response.raise_for_status()
data = response.json()

data["fetch_time"] = datetime.utcnow().isoformat() + "Z"

os.makedirs("data/raw", exist_ok=True)
with open("data/raw/raw_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print("✅ تم جلب البيانات وحفظها في data/raw/raw_data.json")
print(f"⏱️ وقت الجلب: {data['fetch_time']}")
print(f"💰 سعر البيتكوين: ${data['bitcoin']['usd']}")

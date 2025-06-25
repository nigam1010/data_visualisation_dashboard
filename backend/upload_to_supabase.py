import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

with open("jsondata.json", "r", encoding="utf-8") as f:
    json_data = json.load(f)

headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json"
}

for row in json_data:
    response = requests.post(
        f"{SUPABASE_URL}/rest/v1/insights",
        headers=headers,
        json={"data": row}
    )
    if response.status_code != 201:
        print("❌ Error:", response.text)
    else:
        print("✅ Row inserted")

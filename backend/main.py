from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
import httpx

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
SUPABASE_TABLE = "insights"

headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json"
}

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for dev; restrict later
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/data")
async def get_all_data():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{SUPABASE_URL}/rest/v1/{SUPABASE_TABLE}?select=data", headers=headers)
        return [item["data"] for item in response.json()]

@app.get("/filter")
async def get_filtered_data(
    topic: str = Query(None),
    region: str = Query(None),
    sector: str = Query(None),
    pest: str = Query(None),
    source: str = Query(None),
    swot: str = Query(None),
    country: str = Query(None),
    city: str = Query(None),
    end_year: str = Query(None),
):
    filters = {
        "data->>topic": topic,
        "data->>region": region,
        "data->>sector": sector,
        "data->>pestle": pest,
        "data->>source": source,
        "data->>swot": swot,
        "data->>country": country,
        "data->>city": city,
        "data->>end_year": end_year,
    }

    # Build Supabase filter string
    query_string = "&".join(
        [f"{k}=eq.{v}" for k, v in filters.items() if v]
    )

    url = f"{SUPABASE_URL}/rest/v1/{SUPABASE_TABLE}?select=data"
    if query_string:
        url += f"&{query_string}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        return [item["data"] for item in response.json()]

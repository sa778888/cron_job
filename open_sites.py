# open_sites.py
import requests
from datetime import datetime

sites = [
    "https://discord-yef2.onrender.com/",
    "https://portfolioa-five.vercel.app/"
]

for site in sites:
    try:
        response = requests.get(site)
        print(f"[{datetime.now()}] {site} - {response.status_code}")
    except Exception as e:
        print(f"[{datetime.now()}] Failed to reach {site}: {e}")

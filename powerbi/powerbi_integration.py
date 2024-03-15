
import httpx
import os

from dotenv import load_dotenv

load_dotenv()

async def send_to_power_bi(data):
    power_bi_url = os.getenv('POWER_BI_URL')

    headers = {
        "Content-Type": "application/json"
    }
    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.post(power_bi_url, headers=headers, json=data)
        try:
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            print(f"Error al enviar datos a Power BI: {e.response.text}")
            raise

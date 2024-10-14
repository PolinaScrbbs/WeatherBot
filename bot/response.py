from typing import Optional
import aiohttp
from config import API_URL, API_KEY

async def get_weather(city_name: str) -> Optional[dict]:
    async with aiohttp.ClientSession() as session:
        params = {
            "q": city_name,
            "appid": API_KEY,
            "lang": "ru"
        }
        async with session.get(API_URL, params=params) as response:
            if response.status == 200:
                weather_data = await response.json()
                return weather_data
            else:
                return None
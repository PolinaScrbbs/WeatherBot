from datetime import datetime
import pytz
from aiogram.types import Message

async def send_weather_message(message: Message, weather_data: dict):
    city = weather_data['name']
    country = weather_data['sys']['country']
    description = weather_data['weather'][0]['description'].capitalize()
    temp = weather_data['main']['temp']
    feels_like = weather_data['main']['feels_like']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']
    sunrise_timestamp = weather_data['sys']['sunrise']
    sunset_timestamp = weather_data['sys']['sunset']

    moscow_tz = pytz.timezone('Europe/Moscow')
    sunrise_time = datetime.fromtimestamp(sunrise_timestamp, tz=pytz.utc).astimezone(moscow_tz).strftime('%H:%M:%S')
    sunset_time = datetime.fromtimestamp(sunset_timestamp, tz=pytz.utc).astimezone(moscow_tz).strftime('%H:%M:%S')

    await message.answer(
        f'''
Погода в городе {city}, {country}:\n\n
🌤 {description}\n
🌡 Температура: {temp}°C (Ощущается как {feels_like}°C)\n
💧 Влажность: {humidity}%\n
💨 Ветер: {wind_speed} м/с\n
🌅 Восход: {sunrise_time} по московскому времени\n
🌇 Закат: {sunset_time} по московскому времени\n
        '''
    )
from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

API_KEY = 'f01ffdab13e1eb3be69a83df011f3ead'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'


@app.get("/weather/{city}")
async def get_weather(city: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            BASE_URL,
            params={
                "q": city,
                "appid": API_KEY,
                "units": "metric"  # Получение погоды в метрической системе
            }
        )
        data = response.json()

        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=data['message'])

        weather = {
            "city": city,
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }
        return weather

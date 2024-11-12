import asyncio
from typing import Dict, Any

async def getCurrentWeather() -> Dict[str, str]:
    # Simulating API delay
    await asyncio.sleep(1)
    weather = {
        'temperature': "21",
        'unit': "C",
        'forecast': "cloudy"
    }
    return weather

async def getLocation() -> str:
    # Simulating API delay
    await asyncio.sleep(1)
    return "Poopara, Kerala"
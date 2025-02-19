import httpx
import os
from dotenv import load_dotenv

load_dotenv()

class CondoAPI:
    def __init__(self):
        self.base_url = os.getenv("API_URL")
        self.client = httpx.AsyncClient()
    
    async def get_condo_types(self):
        response = await self.client.get(f"{self.base_url}/condo-types/")
        return response.json()
    
    async def send_lead(self, data):
        response = await self.client.post(
            f"{self.base_url}/leads/",
            json=data,
            headers={"Content-Type": "application/json"}
        )
        return response.json()
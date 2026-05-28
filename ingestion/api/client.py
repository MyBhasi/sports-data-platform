import requests
3
from config.settings import API_BASE_URL, API_KEY


class BaseAPIClient:
    def __init__(self):
        self.base_url = API_BASE_URL
        self.headers = {"X-Auth-Token": API_KEY}

    def get(self, endpoint: str, params: dict = None) -> dict:
        response = requests.get(
            f"{self.base_url}/{endpoint}",
            headers=self.headers,
            params=params or {},
        )
        response.raise_for_status()
        return response.json()

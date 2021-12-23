from dataclasses import dataclass
import requests


@dataclass
class RequestClass:
    endpoint: str
    parameters: dict
    headers: str
    json: dict = None
    data: dict = None
    cookies: str = None


    def post_request(self) -> dict:
        results = {}
        try:
            req = requests.post(url=self.endpoint, )
        except requests.exceptions.RequestException as error:
            raise SystemExit(error)
        return results

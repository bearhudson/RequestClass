from dataclasses import dataclass
import requests
from requests.auth import HTTPBasicAuth


@dataclass
class RequestClass:
    endpoint: str
    parameters: dict
    headers: str
    json: dict = None
    data: dict = None
    cookies: str = None
    auth: str = None
    timeout: int = None
    allow_redirects: bool = None
    proxies = str = None
    hooks: str = None
    stream: str = None
    verify: str = None
    cert: str = None

    def post_request(self) -> dict:
        """Make a POST request and return a dictionary."""
        req_results = {}
        try:
            req_results = requests.post(
                url=self.endpoint,
                params=self.parameters,
                headers=self.headers,
            )
        except requests.exceptions.RequestException as error:
            raise SystemExit(error)
        return req_results.json()

    def delete_request(self) -> None:
        """Make a DELETE request. There is no return."""
        try:
            requests.delete(
                url=self.endpoint,
                params=self.parameters,
                headers=self.headers,
            )
        except requests.exceptions.RequestException as error:
            raise SystemExit(error)


    def basic_auth(self):
        """Implements basic authentication and returns an authorization token. Perhaps."""
        pass
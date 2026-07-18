import requests


class BaseAPI:

    def post(self, url, data):

        response = requests.post(
            url,
            data=data,
            timeout=30,
        )

        response.raise_for_status()

        return response.json()
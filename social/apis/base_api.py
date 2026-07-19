import requests


class BaseAPI:

    def post(self, url, data):

        response = requests.post(
            url,
            data=data,
            timeout=30,
        )

        print("=" * 60)
        print("STATUS:", response.status_code)
        print("BODY:", response.text)
        print("=" * 60)

        response.raise_for_status()

        return response.json()
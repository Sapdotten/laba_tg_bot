import json

import requests

from config import Configs


class LabState:
    URL = Configs().back_url

    @classmethod
    def get_state(cls) -> bool:
        return json.loads(requests.get(cls.URL + "/state").text)["state"]

    @classmethod
    def set_state(cls, new_state: bool) -> bool:
        return json.loads(
            requests.post(cls.URL + "/change_state", json={"state": new_state}).text
        )["state"]

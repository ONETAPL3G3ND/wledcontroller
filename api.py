import requests

class Api:
    @classmethod
    def set_led_effect_index(cls, ip: str, index: int):
        print(f"http://{ip}/win&FX={index}")
        requests.get(f"http://{ip}/win&FX={index}")

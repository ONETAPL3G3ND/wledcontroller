import time

from api import Api

if __name__ == "__main__":
    time.sleep(60)
    try:
        Api.set_led_effect_index("192.168.2.117", 9)
        Api.set_led_effect_index("192.168.2.118", 9)
    except:
        ...
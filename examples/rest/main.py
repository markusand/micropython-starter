""" MicroPython start project """

from server import start_server
from lib.wifi import connect_wifi, create_ap

WLAN = {
    "ssid": "network",
    "password": "strong_password",
}


def main():
    """Main function"""
    wlan = connect_wifi(**WLAN, timeout=10) or create_ap(**WLAN)
    start_server()
    return wlan


if __name__ == "__main__":
    main()

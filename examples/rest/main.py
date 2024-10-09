""" MicroPython start project """

from lib.wifi import connect_wifi, create_ap
from server import start_server

WLAN = {
    "ssid": "network",
    "password": "strong_password",
}


def main():
    """Main function"""

    wlan = connect_wifi(**WLAN, timeout=10) or create_ap(**WLAN)

    start_server()


if __name__ == "__main__":
    main()

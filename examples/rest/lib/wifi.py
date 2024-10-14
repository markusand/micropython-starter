""" MicroPython WiFi library """

from network import WLAN, STA_IF, AP_IF
from utime import sleep


def connect_wifi(ssid: str, password: str, timeout=float("inf")) -> WLAN | None:
    """Connect to wlan network"""
    print(f"Connecting to {ssid}", end="")

    wlan = WLAN(STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

    elapsed = 0
    while not wlan.isconnected() and elapsed < timeout:
        print(".", end="")
        sleep(1)
        elapsed += 1

    if not wlan.isconnected():
        print(" failed to connect.")
        return None

    ip, _mask, _gateway, _dns = wlan.ifconfig()
    print(f" connected with IP {ip}.")

    return wlan


def create_ap(ssid: str, password: str) -> WLAN:
    """Create a wlan access point"""
    print(f"Creating wlan AP {ssid}...", end="")

    wlan = WLAN(AP_IF)
    wlan.active(True)
    wlan.config(ssid=ssid, password=password)

    while wlan.active() is False:
        print(".", end="")
        sleep(1)

    ip, _mask, _gateway, _dns = wlan.ifconfig()
    print(f" created with IP {ip}.")

    return wlan

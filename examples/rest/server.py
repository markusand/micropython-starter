""" HTTP Server functions """

from machine import Pin, Signal
from lib.microdot import Microdot

# Assign I/O pins
led = Signal(2, Pin.OUT, invert=True)  # Invert pulldown LED logic

# Create Microdot app
app = Microdot()


def start_server(port=3000, debug=False):
    """Start the server"""
    print(f"Starting server on port {port}")
    app.run(debug=debug, port=port)


@app.get("/")
async def health(_request):
    """Health check"""
    return "Server running!"


@app.get("/led")
async def set_led(request):
    """Set LED state"""
    state: str = request.args.get("state")
    # Change LED state (if required) # pylint: disable-next=W0106
    getattr(led, state)() if state in ["on", "off"] else None
    return {"state": "on" if led.value() else "off"}

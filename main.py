import asyncio
import board
import digitalio
import usb_hid
from adafruit_hid.mouse import Mouse

# Setup HID mouse
mouse = Mouse(usb_hid.devices)

# Set up pins 13 and 14 for scrolling
lPedal = digitalio.DigitalInOut(board.IO13)
rPedal = digitalio.DigitalInOut(board.IO14)
for i in (lPedal,rPedal):
    i.direction = digitalio.Direction.INPUT
    i.pull = digitalio.Pull.DOWN

# Interval (in seconds) for reading the pins
READ_INTERVAL = 0.1


async def upHandler():
    while True:
        # If pin 13 is high, send scroll up
        if rPedal.value:
            # wheel parameter > 0 for scrolling up, adjust the value if needed.
            mouse.move(wheel=1)
            print("up")
        await asyncio.sleep(READ_INTERVAL)


async def downHandler():
    while True:
        # If pin 14 is high, send scroll down
        if lPedal.value:
            # wheel parameter < 0 for scrolling down, adjust the value if needed.
            mouse.move(wheel=-1)
            print("down")
        await asyncio.sleep(READ_INTERVAL)

#Main thing
async def main():
    # Create asynchronous tasks for scrolling
    asyncio.create_task(upHandler())
    asyncio.create_task(downHandler())
    while True:
        await asyncio.sleep(1)
# Start the asyncio event loop.
asyncio.run(main())


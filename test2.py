import time
from luma.led_matrix.device import max7219
from PIL import Image
from luma.core.interface.serial import spi, noop

serial = spi(port=1, device=0, gpio=noop())

device = max7219(serial, width=8, height=8, rotate=0, block_orientation=0)

print("Created device")

newimage = Image.new('1', (8, 8))
newimage.putpixel((0,0), 5)

device.display(newimage)

time.sleep(3)

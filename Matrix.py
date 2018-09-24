#!/usr/bin/env python
# This is the simple card reader

import time

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from PIL import Image
from luma.core.legacy.font import CP437_FONT, proportional
from luma.core.legacy import text, show_message

class Matrix:
    device = None
    """docstring for Matrix"""
    def __init__(self):
        serial = spi(port=1, device=0, gpio=noop())
        self.device = max7219(serial, width=8, height=8, rotate=0, block_orientation=0)

    def DisplayImage(self, image):
        newimage = Image.new('1', (8, 8))
        for i in range(8):
            for j in range(8):
                newimage.putpixel((i,j), image[i][j])
        self.device.display(newimage)

    def ShowMsg(self, msg):
	show_message(self.device, msg, fill="white", \
font=proportional(CP437_FONT), scroll_delay = 0.04)

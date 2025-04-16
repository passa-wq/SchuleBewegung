# Imports
import time
from gpiozero import MotionSensor
from signal import pause
from luma.core.interface.serial import i2c
from luma.oled.device import sh1106
from PIL import Image, ImageDraw, ImageFont
import luma

# Setup
pir = MotionSensor(17) # Bewegungsmelder Setup
serialPort = i2c(port=1, address=0x3c) # Serial Port für Display
oled = sh1106(serialPort, width=128, height=64) # SH1106-OLED initialisieren
font = ImageFont.load_default()
 
print("Geht los!")
 
def mein_callback(channel):
    # Hier kann alternativ eine Anwendung/Befehl etc. gestartet werden.
    print('Bewegungsmelder')
    drawOnMonitor("Bewegungsmelder!")
    oled.clear()
    oled.show()
    
def drawOnMonitor(text):
    oled.clear()
    oled.show()
    
    image = Image.new("1", (oled.width, oled.height))
    draw = ImageDraw.Draw(image)
    
    draw.text((0, 0), text, font=font, fill=255)
    oled.display(image)
    time.sleep(3)

pir.when_motion = mein_callback
pause()


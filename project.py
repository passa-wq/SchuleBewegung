# Imports
import time
from gpiozero import MotionSensor, LED # type: ignore
from signal import pause
from luma.core.interface.serial import i2c
from luma.oled.device import sh1106
from PIL import Image, ImageDraw, ImageFont
import luma

# Setup
pir = MotionSensor(17) # Bewegungsmelder Setup
led = LED(27)
serialPort = i2c(port=1, address=0x3c) # Serial Port für Display
oled = sh1106(serialPort, width=128, height=64) # SH1106-OLED initialisieren
font = ImageFont.load_default()
motionMessage = "Weg hier!"


 
def mein_callback(channel):
    # Hier kann alternativ eine Anwendung/Befehl etc. gestartet werden.
    led.on()
    drawOnMonitor(motionMessage)
    oled.clear()
    oled.show()
    led.off()
    
def drawOnMonitor(text):
    print(text)
    oled.clear()
    oled.show()
    image = Image.new("1", (oled.width, oled.height))
    
    draw = ImageDraw.Draw(image)
    
    draw.text((0, 0), text, font=font, fill=255)
    oled.display(image)
    time.sleep(3)

print("Was soll als Meldung angezeigt werden?:")
motionMessage = input()
print(motionMessage + " wird benutzt")
print("Geht los!")

pir.when_motion = mein_callback
pause()

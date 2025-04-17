# Imports
import time
from gpiozero import MotionSensor, LED, Buzzer # type: ignore
from signal import pause
from luma.core.interface.serial import i2c
from luma.oled.device import sh1106
from PIL import Image, ImageDraw, ImageFont
import luma

# Setup
pir = MotionSensor(17) # Bewegungsmelder Setup
led = LED(27)
bz = Buzzer(22)
serialPort = i2c(port=1, address=0x3c) # Serial Port für Display
oled = sh1106(serialPort, width=128, height=64) # SH1106-OLED initialisieren
font = ImageFont.load_default()
motionMessage = "Weg hier!"

def mein_callback(channel):
    # Hier kann alternativ eine Anwendung/Befehl etc. gestartet werden.
    led.on()
    bz.on()
    drawOnMonitor(motionMessage)
    oled.clear()
    oled.show()
    led.off()
    bz.off()
    
def wrap_text(text, line_lengt=23):
    lines = [text[i:i+line_lengt] for i in range(0, len(text), line_lengt)]
    return '§'.join(lines)

def drawOnMonitor(text):
    print(text)
    oled.clear()
    oled.show()
    image = Image.new("1", (oled.width, oled.height))
    lineCount = 0

    draw = ImageDraw.Draw(image)

    for line in wrap_text(text).split("§"):
        print(line)
        draw.text((0, lineCount), line, font=font, fill=255)
        lineCount += 10
    
    oled.display(image)
    time.sleep(3)

print("Was soll als Meldung angezeigt werden?:")
motionMessage = input()
print(motionMessage + " wird benutzt")
print("Geht los!")

pir.when_motion = mein_callback
pause()
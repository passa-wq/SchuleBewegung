import time
from gpiozero import MotionSensor, LED, Buzzer, Button
from signal import pause
from luma.core.interface.serial import i2c
from luma.oled.device import sh1106
from PIL import Image, ImageDraw, ImageFont

# Setup
pir = MotionSensor(17)
led = LED(27)
bz = Buzzer(22)
button = Button(23)
serialPort = i2c(port=1, address=0x3c)
oled = sh1106(serialPort, width=128, height=64)
font = ImageFont.load_default()

# Anfangszustand: System ist AUS
system_aktiv = False
motion_message = ""

def wrap_text(text, line_length=23):
    return [text[i:i+line_length] for i in range(0, len(text), line_length)]

def draw_on_monitor(text):
    oled.clear()
    image = Image.new("1", (oled.width, oled.height))
    draw = ImageDraw.Draw(image)
    for i, line in enumerate(wrap_text(text)):
        draw.text((0, i * 10), line, font=font, fill=255)
    oled.display(image)

def motion_detected():
    if system_aktiv:
        print("Bewegung erkannt!")
        led.on()
        bz.on()
        draw_on_monitor(motion_message)
        time.sleep(2)
        led.off()
        bz.off()
        oled.clear()
        oled.show()

def button_pressed():
    global system_aktiv, motion_message
    if not system_aktiv:
        print("System wird aktiviert...")
        draw_on_monitor("System wird aktiviert...")
        time.sleep(1)
        
        # Jetzt Nachricht vom Benutzer abfragen
        motion_message = input("Was soll als Meldung angezeigt werden?\n")
        print(f"Meldung gesetzt: '{motion_message}'")
        
        # System aktivieren
        system_aktiv = True
        draw_on_monitor("System ist an")
        print("System ist jetzt aktiv.")
    else:
        print("System wird deaktiviert...")
        system_aktiv = False

# Startanzeige
oled.clear()
oled.show()
draw_on_monitor("Druecke den Knopf, um das System zu aktivieren.")
print("Drücke den Knopf, um das System zu aktivieren.")

# Ereignisse verbinden
pir.when_motion = motion_detected
button.when_pressed = button_pressed

pause()

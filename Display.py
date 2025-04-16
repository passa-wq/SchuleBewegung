from luma.core.interface.serial import i2c
from luma.oled.device import sh1106
from PIL import Image, ImageDraw, ImageFont
import time

# I2C-Verbindung herstellen (Port 1, Adresse 0x3C ist Standard)
serial = i2c(port=1, address=0x3C)

# SH1106-OLED initialisieren
oled = sh1106(serial, width=128, height=64)

# Display leeren
oled.clear()
oled.show()

# Neues Bild vorbereiten
image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)

# Schriftart laden
font = ImageFont.load_default()

# Text zeichnen
draw.text((0, 0), "OLED läuft!", font=font, fill=255)

# Bild anzeigen
oled.display(image)

# Damit der Text stehen bleibt (kannst du anpassen)
time.sleep(10)

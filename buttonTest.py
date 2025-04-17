from gpiozero import Button
from time import sleep

btn = Button(23)
btnPressedCount = 0

while True:
    if (btn.is_active):
        print(btnPressedCount)
        btnPressedCount += 1
        sleep(1)
from gpiozero import Buzzer
from time import sleep

bz = Buzzer(22)

bz.on()
sleep(3)
bz.off()
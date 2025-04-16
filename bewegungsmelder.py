import time
from gpiozero import MotionSensor
from signal import pause

pir = MotionSensor(17)
 
print("Geht los!")
 
def mein_callback(channel):
    # Hier kann alternativ eine Anwendung/Befehl etc. gestartet werden.
    print('Mache Eier du Pimmel!')

pir.when_motion = mein_callback
pause()

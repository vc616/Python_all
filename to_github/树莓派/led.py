from gpiozero import LED
import time


led = LED(21)
while:
    led.on()
    time.sleep(2)
    led.off()
    time.sleep(2)
    


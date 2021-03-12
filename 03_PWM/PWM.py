from machine import Pin, PWM 
import utime

#Set GPIO25 output pwm 
LED  = PWM(Pin(25))

#Set pwm frequency to 1000HZ
LED.freq(10000)

LED_duty = 0
LED_direction = 1

while True:
    LED_duty += LED_direction
    if LED_duty >= 100:
        LED_duty = 100
        LED_direction = -1
    elif LED_duty <= 0:
        LED_duty = 0
        LED_direction = 1
    LED.duty_u16(int(LED_duty * 655.36))
    if LED_duty%5 == 0:
        print(LED_duty)
    utime.sleep(0.01)



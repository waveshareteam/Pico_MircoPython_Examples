from machine import Pin
import utime
#Initialize GPIO15, and set the pull-up input mode
button_num = 15
button = Pin(button_num,Pin.IN,Pin.PULL_UP)

#Initialize GPIO16, and set the output mode
external_led_num =16
external_led = Pin(external_led_num,Pin.OUT)

#Initialize GPIO25, and set the output mode
led_num = 25
led = Pin(led_num,Pin.OUT)

print("button gpio={0}".format(button_num))

while True:
    #led turn off
    led.off()
    #Read button value
    if(button.value()==0):
        utime.sleep(0.01)
        if(button.value()==0):
            #Toggle led 
            external_led.toggle()
            #led turn on
            led.on()
           
            print("button is pressed")
            while(button.value()==0):
                utime.sleep(0.01)
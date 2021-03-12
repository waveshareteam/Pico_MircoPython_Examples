from machine import Pin, ADC 
import utime

#Initialize the ADC channel
ADC0= ADC(Pin(26))
sensor_temp = ADC(4)

while True:

    #Read ADC channel 0 voltage
    reading = ADC0.read_u16()*3.3/65535
    print("ADC0 voltage = {0:.2f}V \r\n".format(reading))
    
    #Temperature is captured using an internal temperature sensor
    reading = sensor_temp.read_u16()*3.3/65535
    temperature = 27 - (reading - 0.706)/0.001721
    print("temperature = {0:.2f}℃ \r\n".format(temperature))
    
    utime.sleep_ms(1000)

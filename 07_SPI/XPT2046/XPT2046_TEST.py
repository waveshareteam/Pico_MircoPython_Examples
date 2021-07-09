from machine import SPI,Pin
import time
     
spi = SPI(1,baudrate=5_000_000,sck=Pin(10),mosi=Pin(11),miso=Pin(12))
IRQ = Pin(17,Pin.IN)
TP_CS =Pin(16,Pin.OUT)

TP_CS(1)

while True:  
    if IRQ() == 0:
        TP_CS(0)  
        spi.write(bytearray([0XD0]))
        Read_date = spi.read(2)
        time.sleep_us(10)
        X_Point=((Read_date[0]<<8)+Read_date[1])>>3
  
        spi.write(bytearray([0X90]))
        Read_date = spi.read(2)
        Y_Point=((Read_date[0]<<8)+Read_date[1])>>3       
        TP_CS(1)
        
        print("******************************")
        print("*********TP_Read_ADC**********")
        print("******************************")
        print("X_Point ={} ".format(X_Point))
        print("Y_Point ={}".format(Y_Point))
    time.sleep(0.5)

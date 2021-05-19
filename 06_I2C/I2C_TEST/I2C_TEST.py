from machine import I2C,Pin
#Initialize the I2C 
i2c = I2C(id=1,scl=Pin(7),sda=Pin(6),freq=100_000)
# Get the address of all devices under the I2C bus
addr_list = i2c.scan()
# Resolving device information
if len(addr_list) == 1:
    who = i2c.readfrom_mem(addr_list[0],0x00,1)
    # Identify ICM20948
    if who[0] == 0xEA :
        print("Just a ICM20948 connected")
    else :
        print("Have a device connected but it is not ICM20948")
# Nothing connected
elif len(addr_list) == 0:
    print("Nothing connected")
# More than one device is connected
else:
    print("More than one device is connected")
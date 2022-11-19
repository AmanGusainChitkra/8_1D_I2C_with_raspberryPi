import smbus
import time
import sys

I2C_ADDR  = 0x23 # light sensor address


bus = smbus.SMBus(1) #configuring the bus rev 

low_res_mode = 0x13	#fixes the mode for light sensor




def convertToNumber(data):  #to convert incoming data to decimal
  result=(data[1] + (256 * data[0]))
  display(result)

def readLight(addr=I2C_ADDR):       #address of I2C is passed
  data = bus.read_i2c_block_data(addr,low_res_mode)
  return convertToNumber(data)

def display(value):     #prints the value of light
    if(value >300):
        print("The light is too bright." + format(value,'.2f') + " lux")
    elif(value > 200 and value < 300):
        print("The light is bright. " + format(value,'.2f') + " lux")
    elif(value > 80 and value < 200):
        print("The light is medium. " + format(value,'.2f') + " lux")    
    elif(value > 20 and value < 80):
        print("The light is dark." + format(value,'.2f') + " lux")
    elif(value > 0 and value < 20):
        print("The light is too dark. " + format(value,'.2f') + " lux")

while True:
    value=readLight()
    time.sleep(0.5)




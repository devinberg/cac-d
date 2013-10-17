import serial
import io

ser = serial.Serial()
ser.baudrate = 9600    #THIS MAY NEED TO BE CHANGED
ser.port = 4                  #opens comm port 3, may need to be changed
print(ser) #prints the stats of the comm port

ser.open()
print(ser.isOpen()) #Tests if the port is open

#The following sends data through the comm port
ser.write(b'F I1M400 R') #This will apparently increment the motor 1 revolution

#The 'F' is to tell the controller to accept input
#The I1M400 follows the IxMyyy format, where x is the motor number and yyy is the amount of steps
#The R tells the controller to run the command

ser.close()
print(ser.isOpen()) #tests if port is closed

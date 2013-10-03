import serial
import io


ser = serial.Serial()
ser.baudrate = 19200
ser.port = 2 #opens comm port 3
print(ser) #prints the stats of the comm port


ser.open()
print(ser.isOpen()) #Tests if the port is open

ser.write(b'F I1M400 R') #This will apparently increment the motor 1 revolution

ser.close()
print(ser.isOpen()) #tests if port is closed

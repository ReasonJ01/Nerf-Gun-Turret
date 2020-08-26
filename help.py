import serial

ard = serial.Serial("COM3", 9600)

ard.write(b"s")
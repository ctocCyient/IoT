import pymodbus
import serial
from pymodbus.pdu import ModbusRequest
from pymodbus.client.sync import ModbusSerialClient as ModbusClient  # initialize a serial RTU client instance
from pymodbus.transaction import ModbusRtuFramer
#import RPi.GPIO as GPIO
# Read data from rs485 using pymodbus python using Rs485-USB converter


# count= the number of registers to read
# unit= the slave unit this request is targeting
# address= the starting address to read from
def read_data_rs485_holding():
    client= ModbusClient(method = "rtu", port="/dev/ttyUSB0",stopbits = 1, bytesize = 8, parity = 'N',baudrate= 9600)
    #Connect to the serial modbus server
    connection = client.connect()
    print(connection)
    #Starting add, num of reg to read, slave unit.
    result= client.read_holding_registers(0x17,2,unit= 1)
    print(result)
    #Closes the underlying socket connection
    client.close()
    print(result.registers[0]*0.001)
    return result.registers[0]

read_data_rs485_holding()
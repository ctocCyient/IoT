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
def read_data_rs485_holding(configuration,device):
    client= ModbusClient(method = "rtu", port=configuration["port"],stopbits = configuration["stop_bit"], bytesize = 8, parity = configuration["parity"],baudrate= 9600)
    #Connect to the serial modbus server
    connection = client.connect()
    print(connection)
    #Starting add, num of reg to read, slave unit.   
    result= client.read_holding_registers(int(device["Register_address"],16),2,unit= 1)
    print(int(device["Register_address"],16))
    #Closes the underlying socket connection
    client.close()
    print(result.registers[0])
    return result.registers[0]*device["Multiplier"]


def read_data_IO(pin,mode):
    """GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    return GPIO.input(4)"""
    return 0



def write_data_rs485(configuration, device):
    client= ModbusClient(method = "rtu", port="/dev/ttyUSB0",stopbits = 1, bytesize = 8, parity = 'E',baudrate= 9600)
    #Connect to the serial modbus server
    connection = client.connect()
    print(connection)
    #Starting add, num of reg to read, slave unit.
    #result= client.read_holding_registers(0x00,2,unit= 0xff)
    #print(result)
    client.write_register(0x00,"1")
    #Closes the underlying socket connection
    client.close()


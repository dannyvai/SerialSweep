import serial

SERIAL_PORT = '/dev/ttyUSB0'

baudrate_list = [50, 75, 110, 134, 150, 200, 300, 600, 1200, 1800, 2400, 4800, 9600, 19200, 38400, 57600, 115200]
bytesize_list = [serial.FIVEBITS, serial.SIXBITS, serial.SEVENBITS, serial.EIGHTBITS]
parity_list = [serial.PARITY_NONE, serial.PARITY_EVEN, serial.PARITY_ODD]
#serial.PARITY_MARK, serial.PARITY_SPACE]
stopbits_list = [serial.STOPBITS_ONE,serial.STOPBITS_ONE_POINT_FIVE,serial.STOPBITS_TWO]

for baudrate in baudrate_list:
    for bytesize in bytesize_list:
        for parity in parity_list:
	    for stopbits in stopbits_list:
		ser = serial.Serial(SERIAL_PORT,baudrate=baudrate,bytesize=bytesize,parity=parity,stopbits=stopbits,timeout=1)
		ret = ser.read(1)
		if len(ret) > 0:
			print ser

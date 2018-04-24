import re
import datetime
import json
import csv
import subprocess
import serial
import serial.tools.list_ports
import requests

vidpidList = ["1A86:7523"]  # TODO: add VID:PID of other devices if required

devPath = ""
devPath_re = re.compile(r"/dev/tty[\w|\d]*\d")
for vidpid in vidpidList:
    # portListRaw = subprocess.check_output("python3 -m serial.tools.list_ports {}".format(item))  # Obtain dev path for items matching vidpid
    portDict = serial.tools.list_ports.grep(vidpid)
    for port in portDict:
        devPath = port.device
print(devPath)
while True:
    with serial.Serial(devPath, timeout=2) as ser:
        # line = ser.read(111)
        line = ser.readline()
        print(line)
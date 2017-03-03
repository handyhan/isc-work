import csv


time = []
temp = []

def convert_time(tm):
    tm = datetine.strftime(tm, '%Y-%m-%dT%H:%M:%S.%f')
    return tm

def convert_temp(temp):
    value = temp.strip('+').strip('C').lstrip('0')
    return float(value) + 273.15    

with open('serial-temperature.tsv','r') as reader:
    line = reader.readlines()
    for line in

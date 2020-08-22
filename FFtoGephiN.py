#!/usr/bin/python
from csv import reader

with open('FTDNA_FF_FILE.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    i = 0

    print("Id,Label,timeset")
    print("0,Your Name,")
    for row in csv_reader:
        if i > 1:
            print('%d,%s,' %(i-1,row[0]))
        i += 1

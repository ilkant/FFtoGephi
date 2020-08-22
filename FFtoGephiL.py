#!/usr/bin/python
from csv import reader

with open('FTDNA_FF_FILE.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    i = 0
    
    print("Source,Target,Type,Id,Label,timeset,Weight")

    for row in csv_reader:
        i += 1
        if i > 1:
            print('%d,%d,Undirected,%d,,,%d' %(0,i-1,i-2,int(float(row[7]))))

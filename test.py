# This program starts to making csv files to Gephi to display n persons weighted march graph
# You can use this enjoy your dna. If you modify, please send the modified code to me.
#
# FFtoGephi Main
# (c) Ilpo Kantonen 2020
# ilpo@iki.fi

#!/usr/bin/python
# -*- coding: latin-1 -*-

import os.path
from os import path
import sys
#import fileinput
import csv
from csv import reader
from datetime import datetime

from Kit import Kit
from MatchList import MatchList
from ForGephi import ForGephi
#import ForGephi.py
#from ForGephi import setMax

#-----------------------------------------------------------------------------------------------------------    
#----------------------------------------- Main ------------------------------------------------------------    
#-----------------------------------------------------------------------------------------------------------    
i=0
if len(sys.argv) != 1:
    if not os.path.isfile(sys.argv[1]):
        print ("Error: Source file not exist")
        exit(0)

    # Set maximum drawn dna-matches to Gephi charts
    ForGephi.setMax(200)
 
    # Fresh means that it is downloaded today. Remember timezone. It makes some harm.
    freshkits = []
    freshkits = MatchList.getFreshMatchLists( str( sys.argv[1] ) )

    ind30=0
    offsetN = 0
    offsetL = 0
    
    for fresh in freshkits:
        if ind30 == 0:
            offsetN = ForGephi.addNames1(fresh)
            offsetL = ForGephi.addLinks1(fresh)
            ind30 += 1
        else:
            offsetN = ForGephi.addNames2(fresh,offsetN)
            offsetL = ForGephi.addLinks2(fresh,offsetL,200)
    print('Done.')
else:
    print('Usage: python kits.py kits.csv')
#-----------------------------------------------------------------------------------------------------------    

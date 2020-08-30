from datetime import datetime
import csv
from csv import reader
import os.path
from os import path

#--------------------------------------------------------------------------------------------------------------- 
#---------------------------------------------------------------------------------------------------------------    
#------------------------------------ MatchList ----------------------------------------------------------------    
#---------------------------------------------------------------------------------------------------------------    
class MatchList:
#    @static
    dlpath = '/home/user/Download/'
    dlen = 0
    now_s = 0
    sfname = ''
    namesfile ='names.csv'
    linksfile = 'links.csv'

    #-----------------------------------------------------------------------------------------------------------    
    #-------------------------------- Constructor --------------------------------------------------------------    
    #-----------------------------------------------------------------------------------------------------------    
    def __init__(self, id_p = 0):
        i = 0
        self.dlen = len(self.dlpath)
        now_s = datetime.now()
        self.sfname = dlpath + id_p + '_Family_Finder_Matches_' + (now_s.strftime("%Y%m%d")) + '.csv'
        print(self.sfname)
    #-----------------------------------------------------------------------------------------------------------    

    #-----------------------------------------------------------------------------------------------------------    
    #-------------------------------- readFiles ----------------------------------------------------------------    
    #-----------------------------------------------------------------------------------------------------------    
    def readFiles():
        kitsf = open('kits.csv')
        kcsv = csv.reader(kitsf)
        i=0
        for k in kcsv:
            names.add(i,k[o])
            mkname()
    #-----------------------------------------------------------------------------------------------------------    

    #-----------------------------------------------------------------------------------------------------------    
    #-------------------------------- getFreshMatchlists -------------------------------------------------------    
    #-----------------------------------------------------------------------------------------------------------    
    @staticmethod
    def getFreshMatchLists(fname_p):
        dlpath = '/home/user/Downloads/'
        now = datetime.now()
        dlen = len(dlpath)
        foundf = []

        with open(fname_p, 'r') as read_obj2:
            kcsv = reader(read_obj2)
            i=0
            for f in kcsv:
                s = ('%s%s_Family_Finder_Matches_%s.csv' %(dlpath,f[0],(now.strftime("%Y%m%d"))) )
                if os.path.isfile(s):
                    foundf.append(s)
                i += 1        
        return(foundf)
    #-----------------------------------------------------------------------------------------------------------

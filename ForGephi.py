# FORGEPHI Tools which writes input files names.csv and links.csv to Gephi inputs from FTDNA FF match lists
#
# (c) Ilpo Kantonen 2020

import csv
from csv import reader

#-----------------------------------------------------------------------------------------------------------    
#----------------------------------------- ForGephi --------------------------------------------------------    
#-----------------------------------------------------------------------------------------------------------    
class ForGephi:
    indN = 0
    indL = 0
    firstname = ''
    foundkitlist = []
    max_e = 0
    fnameN = 'names.csv'
    fnameL = 'links.csv'

    #-------------------------------------------------------------------------------------------------------    
    #----------------------------------------- Constructor -------------------------------------------------    
    #-------------------------------------------------------------------------------------------------------    
    def __init__():
        indN = 0
        indL = 0
        max_e = 200
    #-------------------------------------------------------------------------------------------------------    

    #-------------------------------------------------------------------------------------------------------    
    #----------------------------------------- setMax ------------------------------------------------------    
    #-------------------------------------------------------------------------------------------------------    
    @staticmethod
    def setMax(count):
        max_e = count
    #-------------------------------------------------------------------------------------------------------    

    #-------------------------------------------------------------------------------------------------------    
    #----------------------------------------- addNames1 ---------------------------------------------------    
    #-------------------------------------------------------------------------------------------------------    
    # fname     - Match file
    @staticmethod
    def addNames1(fname):
        fnameN = 'names.csv'
        
        nf = open(fnameN, "w")
        nf.write("Id,Label,timeset\n")
        dingeli = '0,Ilpo  Kantonen,\n'
        nf.write(dingeli)
        count_writed = 0

        max_e = 200
        with open(fname, 'r') as read_obj2:
            i=0
            csv_reader = reader(read_obj2)
            for row2 in csv_reader:
                # Skip header line of match list
                if i > 0:
                    if max_e > 0:
                        if count_writed < max_e-1:
                            count_writed += 1
                            nf.write('%d,%s,\n' %(count_writed,row2[0]))
                i += 1
        nf.close()
        return(count_writed+1)

    #-------------------------------------------------------------------------------------------------------    
    #----------------------------------------- addNames2 ---------------------------------------------------    
    #-------------------------------------------------------------------------------------------------------    
    # fname     - Match file
    # offset    - Count of links in previous(es) file(s)
    @staticmethod
    def addNames2(fname,offset):
        rows = []
        # Remember content of names file before it changes
        fnameN = 'names.csv'
        max_e = 200
        
        with open(fnameN, 'r') as read_obj4:
            i=0
            csv4_reader = reader(read_obj4)
            for row4 in csv4_reader:
                # Skip header line of match list
                if i > 0:
                    rows.append(row4)
                i += 1

        nf = open(fnameN, "a")
        u = 0
        count_writed = 0

        with open(fname, 'r') as read_obj2:
            csv2_reader = reader(read_obj2)
            i=0
            sama = 0
            j=0
            for row2 in csv2_reader:
                if j > 0:
                    sama=0
                    xyz=0
                    numero_str = ''
                    numero = 0
                    for xyzz in rows:
                        if row2[0] in rows[xyz]:
                            sama = 1
                            break
                        xyz += 1
                    if sama == 0:
                        if max_e > 0:
                            if count_writed < max_e-1:
                                count_writed += 1
                                nf.write('%d,%s,\n' %(offset,row2[0]))
                                offset += 1
                    j += 1
                j += 1
            ind=u
            nf.close()
            return(offset+i)

    #-------------------------------------------------------------------------------------------------------    
    #----------------------------------------- addLinks1 ---------------------------------------------------    
    #-------------------------------------------------------------------------------------------------------    
    # fname     - Match file
    # max_e       - max_eimum amount of people which is counted in
    @staticmethod    
    def addLinks1(fname):
        spn=0
        count_writed = 0

        max_e = 200
        # Open output file and write header and first person from to it
        fnameL = 'links.csv'
        nf = open(fnameL, "w")
        nf.write("Source,Target,Type,Id,Label,timeset,Weight\n")
        nf.write('%d,%d,Undirected,%d,,,%d\n' %(0,0,0,0))

        writtenlinks = 0
        nf = open(fnameL, "a")
        with open(fname, 'r') as read_obj2:
            i=0
            csv_reader = reader(read_obj2)
            for row2 in csv_reader:
                # Skip header line of match list
                if i > 1:
                    if max_e > 0:
                        if i < max_e:
                            count_writed += 1
                            nf.write('%d,%d,Undirected,%d,,,%d\n' %(0,i-1,i-2,int(float(row2[7]))))
                            writtenlinks += 1
                i += 1
        nf.close()
        return(writtenlinks)
    #-------------------------------------------------------------------------------------------------------    


    #-------------------------------------------------------------------------------------------------------    
    #----------------------------------------- findName ----------------------------------------------------    
    #-------------------------------------------------------------------------------------------------------    
    # name      - Who is searched
    # return    - Index on list where found. -1 if not found
    def findName(name):
        with open(filen, 'r') as read_obj:
            csv_reader = reader(read_obj)
            i = 0
            for a in csv_reader:
                i += 1
                if a[1] == name:
                   break
        return(i-1)
    #-------------------------------------------------------------------------------------------------------    


    #-------------------------------------------------------------------------------------------------------    
    #----------------------------------------- addLinks2 ---------------------------------------------------    
    #-------------------------------------------------------------------------------------------------------    
    # fname     - Match file
    # offset    - Count of links in previous(es) file(s)
    # person    - from who the links are
    @staticmethod    
    def addLinks2(fname,offset,sourcepersonname):
        # person = who links they are
        links = []
        names = []
        u=0
        count_writed = 0
        fnameL = 'links.csv'
        
        # Remember content of links file before it changes
        with open(fnameL, 'r') as read_obj4:
            i=0
            csv4_reader = reader(read_obj4)
            for row4 in csv4_reader:
                # Skip header line of match list
                if i > 0:
                    links.append(row4)
                i += 1

        # Find source persons index, so you can write his or hers links to links.csv
        fnameN = 'names.csv'
        names = []
        inteksi = 0
        fnamesN = 'names.csv'
        with open(fnamesN, 'r') as read_obj7:
            csv7_reader = reader(read_obj7)
            for n7 in csv7_reader:
                if inteksi > 0:
                    names.append(n7)
                inteksi += 1

        i_tmp=0
        for etsihanta in names:
            if etsihanta[1] == sourcepersonname:
                break
            else:
                i_tmp += 1
                
        sourceindex = i_tmp

        max_e = 200
        writtenlinks=0
        
        fnameL = 'links.csv'
        nf = open(fnameL, "a")


        with open(fname, 'r') as read_obj12:
            i=0

            csv_reader = reader(read_obj12)
            for row12 in csv_reader:
                # Skip header line of match list
                if i > 1:
                    if max_e > 0:
                        if i < max_e:
                            count_writed += 1

                            i_tmp=0
                            for etsihanta in names:
                                sintso = ''
                                sintso = row12[1]
                                sintso += row12[2]
                                
                                if etsihanta[1] == row12[0]:
                                    break
                                else:
                                    i_tmp += 1
                
                            targetindex = i_tmp

                            nf.write('%d,%d,Undirected,%d,,,%d\n' %(sourceindex,targetindex,offset+i-2,int(float(row12[7]))))
                            writtenlinks += 1
                i += 1
        nf.close()
        return(offset+writtenlinks)
    #-------------------------------------------------------------------------------------------------------    

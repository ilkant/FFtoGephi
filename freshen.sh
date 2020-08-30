#!/bin/bash
OLD=$1
NEW=$(date +'%Y%m%d')
Polku='/home/user/Downloads/'
Ftdna='_Family_Finder_Matches_'
Ftype='.csv'

for Item in 'kit1id' 'kit2id' 'kit3id' 'kit4id' 'kit5id' ;
  do
    mv $Polku$Item$Ftdna$OLD$Type $Polku$Item$Ftdna$NEW$FType
  done

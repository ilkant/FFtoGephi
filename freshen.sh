#!/bin/bash
OLD=$1
NEW=$(date +'%Y%m%d')
Polku='/home/user/Downloads/'
Ftdna='_Family_Finder_Matches_'
Ftype='.csv'

for Item in 'kit1id' 'kit1id' 'kit1id' 'kit1id' ;
  do
    mv $Polku$Item$Ftdna$OLD$Type $Polku$Item$Ftdna$NEW$FType
  done

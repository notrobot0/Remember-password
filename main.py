#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from itertools import product 
#       first letter      second letter    third letter ............
arr=[['S','s','с','С'],['п','П','g','G'],['Р','р','r','R']]
password = ["".join(res) for res in product(*arr)]
for yra in password:
   print(yra)
        

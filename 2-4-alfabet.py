""" Języki skryptowe - Cwiczenia - Rafał Stepkowski GD30982 - alfabet - zajecia 2
Wydrukuj alfabet w formacie: AaBbCcDd….., a następnie w formacie:
aAbBcCdD….."""

#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import time

print("Alfabet w porządku duża litera, mała litera:")
x = 0
for i in range(65, 91):
    litera = chr(i)
    x += 1
    tmp = litera + litera.lower()
    if i > 65 and x % 5 == 0:
        x = 0
        
    print(tmp)

x = -1
print("\nAlfabet w porządku małą litera, duża litera:")
for i in range(65, 91):
    litera = chr(i)
    x += 1
    tmp = litera.lower() + litera.upper()
    if i > 65 and x % 5 == 0:
        x = 0
        tmp += "\n"
    print(tmp, end=" ")
    
time.sleep(60)

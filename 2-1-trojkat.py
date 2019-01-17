""" Zadanie - arkusz 2 - zadanie 1 - Rafał Stępkowski GD30982 -

Napisz program, który na podstawie danych pobranych od użytkownika, czyli
długości boków, sprawdza, czy da się zbudować trójkąt i czy jest to trójkąt
prostokątny. Jeżeli da się zbudować trójkąt, należy wydrukować jego obwód i
pole, w przeciwnym wypadku komunikat, że nie da się utworzyć trójkąta. """

#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import math  

op = "t"  
while op != "n":  
    dane = input("Podaj 3 boki trójkąta (oddzielone przecinkami): ")

    lista = []  
    for x in dane.split(","):
        lista.append(int(x))  
    a, b, c = lista  
    
    print("Podane boki to: ", a, b, c)

    if a + b > c and a + c > b and b + c > a:  
        print("Prawidłowe wymiary boków, można zbudować trójkąt.")
        
        if (a**2 + b**2 == c**2 or
                a**2 + c**2 == b**2 or
                b**2 + c**2 == a**2):
            print("Trójkąt prostokątny!")

        print("Obwód wynosi:", (a + b + c))
        p = 0.5 * (a + b + c)  
        P = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print("Pole wynosi:", P)
        op = "n"  
    else:
        print("Z podanych odcinków nie można utworzyć trójkąta prostokątnego.")
        op = input("Spróbujesz jeszcze raz (t/n): ")

print("3maj się")
input("\n\nAby zakonczyc program, nacisnij Enter.")


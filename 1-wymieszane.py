""" Języki skryptowe - Ćwiczenia - Rafał Stępkowski GD30982 -

Zadanie 3 - Popraw program Wymieszane litery tak, żeby każdemu słowu towarzyszyła
podpowiedź. Gracz powinien mieć możliwość zobaczenia podpowiedzi, jeśli
utknie w martwym punkcie. Dodaj system punktacji, który nagradza graczy
rozwiązujących anagram bez uciekania się do podpowiedzi. """

#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import random as rm
 
EXAMPLE = ("Mietek",
         "Heniek",
         "Zbyszek")
 
correct = rm.choice(EXAMPLE)
 
poprawne = correct
 
pomieszane = ""
 
while correct:
    pozycja = rm.randrange(len(correct))
    pomieszane += correct[pozycja]
    correct = correct[:pozycja] + correct[(pozycja + 1):]
 
print("3...2...1  Zaczynamy")
print("Zgadnij wyraz: ",pomieszane)
 
gosc = input ("zgaduj: ")
x=0
z=0
p = ""
while gosc != poprawne and gosc != "":
    print("zle")
    x+=1
    if x>=3:
        print("Nie udało Ci się zgadnąć w 3 ruchach")
        p = str(input("Potrzebujesz pomocy? Jeśli tak naciśnij y, jeśli wolisz zgadywać bez podpowiedzi naciśnij n: "))
        if p == "y":
            print("pierwsze dwie litery to: ",poprawne[:2])
            z+=1
        elif p == "n":
            print("ok probuj dalej")
    gosc = input("spróbuj jeszcze raz: \n")
 
if gosc == poprawne and z==0:
    print ("brawo, zgadłeś bez podpowiedzi otrzymujesz 3 punkty")
elif gosc == poprawne and z==1:
    print ("brawo, udało Ci się, z podpowiedzią. Otrzymujesz 2 punkty")
elif gosc == poprawne and z>=2:
    print (" otrzymujesz 1ptk")
 
print("Dziękuję za udział w grze.")
input("\n\nAby zakończyć program, naciśnij klawisz Enter.")

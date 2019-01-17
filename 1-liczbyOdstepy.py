""" Języki skryptowe - Cwiczenia - Rafał Stepkowski GD30982 -
Napisz program, który liczy za użytkownika. Umożliwi użytkownikowi
wprowadzenie liczby początkowej, liczby końcowej i wielkości odstępu między kolejnymi
liczbami. """

#! /usr/bin/env python3
# -*- coding: utf-8 -*-

start = int(input("Podaj liczbe poczatkowa: "))
finish = int(input("Podaj liczbe koncowa: "))
jump = int(input("Podaj wielkosc odstepu miedzy kolejnymi liczbami: "))
 
for digit in range(start, finish, jump):
   print(digit, end=" ")
 
input("\n\nAby zakonczyc program, nacisnij Enter.")

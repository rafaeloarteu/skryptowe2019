""" Języki skryptowe - Cwiczenia - Rafał Stepkowski GD30982 - zadanie oceny

Napisz program, który umożliwi wprowadzanie ocen z podanego przedmiotu,
następnie policzy i wyświetla średnią, medianę i odchylenie standardowe
wprowadzonych ocen. Funkcje pomocnicze i statystyczne umieść w osobnym
module. """

""" Modul """

#! /usr/bin/env python3
# -*- coding: utf-8 -*-


import math  


def drukuj(co, kom="Sekwencja zawiera: "):
    print(kom)
    for i in co:
        print(i, end=" ")


def srednia(oceny):
    suma = sum(oceny)
    return suma / float(len(oceny))


def mediana(oceny):
  
    oceny.sort()
    if len(oceny) % 2 == 0:  
        half = int(len(oceny) / 2)
        
        return float(sum(oceny[half - 1:half + 1])) / 2.0
    else:  
        return oceny[len(oceny) / 2]


def wariancja(oceny, srednia):

    sigma = 0.0
    for ocena in oceny:
        sigma += (ocena - srednia)**2
    return sigma / len(oceny)


def odchylenie(oceny, srednia):  
    w = wariancja(oceny, srednia)
    return math.sqrt(w)


""" Języki skryptowe - Cwiczenia - Rafał Stepkowski GD30982 - zadanie oceny

Napisz program, który umożliwi wprowadzanie ocen z podanego przedmiotu,
następnie policzy i wyświetla średnią, medianę i odchylenie standardowe
wprowadzonych ocen. Funkcje pomocnicze i statystyczne umieść w osobnym
module. """

#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import time

""" Modul """

from modul import drukuj, srednia, mediana, odchylenie


def main(args):
    przedmioty = set(['geografia', 'historia'])  
    drukuj(przedmioty, "Lista przedmiotów : ")

    print("\nAby przerwać wprowadzanie przedmiotów, naciśnij Enter.")
    while True:
        przedmiot = input("Podaj nazwę przedmiotu: ")
        if len(przedmiot):
            if przedmiot in przedmioty:  
                print("Przedmiot już wystepuje")
            przedmioty.add(przedmiot)  
        else:
            drukuj(przedmioty, "\nTwoje przedmioty: ")
            przedmiot = input("\nZ którego przedmiotu chcesz wprowadzić oceny? ")
            
            if przedmiot not in przedmioty:
                print("Brak przedmiotu, możesz go dodać.")
            else:
                break  

    oceny = []  
    ocena = None  
    print("\nAby przerwać wprowadzanie ocen, podaj 0 (zero).")

    while not ocena:
        try:
            ocena = int(input("Podaj ocenę (1-6): "))
            if (ocena > 0 and ocena < 7):
                oceny.append(float(ocena))
            elif ocena == 0:
                break
            else:
                print("Błędna ocena.")
            ocena = None
        except ValueError:
            print("Błędne dane!")

    drukuj(oceny, przedmiot.capitalize() + " - wprowadzone oceny: ")
    s = srednia(oceny)  
    m = mediana(oceny)  
    o = odchylenie(oceny, s)  
    print("\nŚrednia: {0:5.2f}".format(s))
    print("Mediana: {0:5.2f}\nOdchylenie: {1:5.2f}".format(m, o))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

os.system("pause")




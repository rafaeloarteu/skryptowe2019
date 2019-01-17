""" Języki skryptowe - Cwiczenia - Rafał Stepkowski GD30982 -Zadanie 3
- zajecia 2

Pobierz od użytkownika n liczb i zapisz je w liście. Wydrukuj:
1. elementy listy i ich indeksy,
2. elementy w odwrotnej kolejności,
3. posortowane elementy.
4. Usuń z listy pierwsze wystąpienie elementu podanego przez użytkownika.
5. Usuń z listy element o podanym indeksie.
6. Podaj ilość wystąpień oraz indeks pierwszego wystąpienia podanego elementu.
7. Wybierz z listy elementy od indeksu i do j. """


#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint

ile = int(input("Ile liczb wylosować? "))
lista = []  
for i in range(0, ile):
    lista.append(randint(0, 100))
print(lista)

print("Dodawanie elementów na końcu listy")
for i in range(0, 3):
    liczba = int(input("Podaj liczbę: "))
    lista.append(liczba)
print(lista)

print("Zawartość listy ([indeks] wartość):")
for i, v in enumerate(lista):
    print("[", i, "]", v)

print("Elementy w odwróconym porządku:")
for e in reversed(lista):
    print(e, end=" ")

print()
print("Elementy posortowane rosnąco:")
for e in sorted(lista):
    print(e, end=" ")

print()
e = int(input("Którą liczbę usunąć? "))
lista.remove(e)
print(lista)

print("Wstawianie elementów do listy")
a, i = eval(input("Podaj element i indeks oddzielone przecinkiem: "))
lista.insert(i, a)
print(lista)

print("Wyszukiwanie i zliczanie elementu w liście")
e = int(input("Podaj liczbę: "))
print("Liczba wystąpień: ")
print(lista.count(e))
print("Indeks pierwszego wystąpienia: ")
if lista.count(e):
    print(lista.index(e))
else:
    print("Brak elementu w liście")

print("Pobieramy ostatni element z listy: ")
print(lista.pop())
print(lista)

print("Część listy :")
i, j = eval(input("Podaj indeks początkowy i końcowy oddzielone przecinkiem: "))
print(lista[i:j])

print()
print("Tupla to lista niemodyfikowalna.")
print("Próba zmiany tupli generuje błąd:")
tupla = tuple(lista)
tupla[0] = 100

input("\n\nAby zakonczyc program, nacisnij Enter.")

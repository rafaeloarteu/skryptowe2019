""" Skryptowe - Python - Rafal Stepkowski - GD30982 -

Napisz program, który pobierze
od użytkownika ilość ruchów
jaką ma wykonać cząstka, a
następnie narysuje
wygenerowane losowo ruch tej
cząstki

cząsteczka, której ruch będziemy śledzić, znajduje się w początku układu współrzędnych (0, 0);
w każdym ruchu cząsteczka przemieszcza się o stały wektor o wartości 1;
kierunek ruchu wyznaczać będziemy losując kąt z zakresu <0; 2Pi>;
współrzędne kolejnego położenia cząsteczki wyliczać będziemy ze wzorów:
x_n = x_{n-1} + r * cos(\phi)

y_n = y_{n-1} + r * sin(\phi)

– gdzie: r – długość jednego kroku, \phi – kąt wskazujący kierunek ruchu w odniesieniu do osi OX.

końcowy wektor przesunięcia obliczymy ze wzoru: |s| = \sqrt{(x^2 + y^2)}"""

#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import random
import matplotlib.pyplot as plt

n = int(input("Ile ruchów? "))
x = y = 0
lx = [0]
ly = [0]

for i in range(0, n):

    rad = float(random.randint(0, 360)) * np.pi / 180
    x = x + np.cos(rad)  
    y = y + np.sin(rad) 
  
    lx.append(x)
    ly.append(y)

print(lx, ly)

s = np.fabs(np.sqrt(x**2 + y**2))
print("Wektor przesunięcia:", s)
plt.plot(lx, ly, "o:", color="blue", linewidth=2, alpha=0.5)
plt.legend(["Dane x, y\nPrzemieszczenie: " + str(s)], loc="upper left")
plt.xlabel("lx")
plt.ylabel("ly")
plt.title("Ruchy Browna")
plt.grid(True)
plt.show()

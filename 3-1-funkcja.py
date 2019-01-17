""" Skryptowe - Python - Rafal Stepkowski - GD30982 -

Napisz program, którego
efektem będzie (patrz w prawo),
wykres funkcji f(x) = a*x + b,
gdzie x = <-10;10>, natomiast
a i b będzie pobierane od
użytkownika. Na wykresie
powinna się pokazać informacja
czy to jest funkcja rosnąca,
malejąca czy stała"""


#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pylab
import numpy as np
import matplotlib.pyplot as plt

a = int(input('Podaj współczynnik a: '))
b = int(input('Podaj współczynnik b: '))
x = range(-10, 10)  
txt = "tekst"

y = [a * i + b for i in x]  

if (a > 0):
    txt = "funkcja rosnaca"
else:
    txt = "funkcja malejaca"

plt.plot(x, y)
plt.title('Wykres f(x) = a*x + b')
plt.title(txt)
plt.grid(True)
plt.show()

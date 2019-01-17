""" Skryptowe - Python - Rafal Stepkowski - GD30982 -

Wykonaj wykres funkcji:
• f(x) = x/(-3) + a dla x <= 0,
• f(x) = x*x/3 dla x >= 0,
• gdzie x = <-10;10> z krokiem 0.5.
• Współczynnik a podaje
użytkownik. Na jednym
wykresie. Wstaw tytuł wykresu,
nazwy osi, legendę oraz wy
pozycjonuj osie liczbowe"""


#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pylab
import numpy as np
import matplotlib.pyplot as plt

x = pylab.arange(-10, 10, 0.5)  
a = int(input("Podaj współczynnik a: "))
y1 = [i / -3 + a for i in x if i <= 0]
y2 = [i**2 / 3 for i in x if i >= 0]

print(x, len(x))
print(y1, len(y1))


plt.plot(x[:len(y1)], y1, x[-len(y2):], y2)
plt.title('Wykres f(x)')
plt.legend(('dane y1 = x/(-3)+a','dane y2 = x^2/3'))
plt.xlabel('os x')
plt.ylabel('os y')
plt.grid(True)
plt.show()

""" Programowanie skryptowe - Zadanie - zajecia 1 - Rafał Stępkowski - GD 30982

Napisz program „Kalkulator napiwku”, w którym użytkownik wprowadza sumę ogólną
z rachunku wystawionego przez restaurację.
Program powinien potem wyświetlić dwie kwoty napiwku w wysokości 15 i 20%"""

kwota = float(input("Podaj wysokość rachunku : "))
kwota15 = kwota * 15/100
kwota20 = kwota * 20/100
print ("Napiwek w wysokośći 15% to :", kwota15, "zl") 
print ("Napiwek w wysokości 20% to :", kwota20, "zl")

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")

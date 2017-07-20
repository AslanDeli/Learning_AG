import os
import sys

print("KALKULATOR")
n1 = input("Podaj pierwsza liczbe: ")
n2 = input ("Podaj drugą liczbe: ")
wyb = input (" 1.DODAWANIE\n 2.ODEJMOWANIE\n 3.MNOŻENIE\n 4.DZIELENIE\n ")
num1=int(n1)
num2=int(n2)
def calc(wyb):
    wynik = "ERROR"
    if wyb=="1":
        wynik = num1 + num2
    elif wyb=="2":
        wynik = num1 - num2
    elif wyb=="3":
        wynik = num1*num2
    elif wyb=="4":
        wynik = num1 / num2
        
    print(suma)


calc(wyb)

xD = input("Komentarz: ")
print (xD)

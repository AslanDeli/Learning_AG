import random
import os
import sysconfig

print("KALKULATOR")
n1 = input("Podaj pierwsza liczbe")
n2 = input ("Podaj drugą liczbe")
wyb = input ("1.DODAWANIE  2.ODEJMOWANIE  3.MNOŻENIE 4. DZIELENIE")
num1=int(n1)
num2=int(n2)
def calc(wyb):
    suma = wyb
    if wyb=="1":
        suma = num1 + num2
    elif wyb=="2":
        suma = num1 - num2
    elif wyb=="3":
        suma = num1*num2
    elif wyb=="4":
        suma = num1 / num2
    else:
        suma = "ERROR"
    print(suma)


calc(wyb)

xD = input("heelo")
print (xD)
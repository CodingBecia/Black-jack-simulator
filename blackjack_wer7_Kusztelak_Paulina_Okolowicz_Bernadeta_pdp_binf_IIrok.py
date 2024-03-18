#Kusztelak Paulina
#Bernadeta Okołowicz
#Bioinformatyka, II rok
#Paradygmaty programowania

#imporotwanie modułów.
import random
from functools import reduce

#inicjalizacja talii kart oraz jej tasowanie.
def tasuj_talie():
    talia = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
    random.shuffle(talia)
    return talia

#rozdanie 2 kart dla graczy.
def rozdaj_karty(talia):
    return [talia.pop(), talia.pop()]

#przekształcenie ręki na string.
def reprezentuj_reke(reka):
    return ','.join(str(karta) for karta in reka)

#liczymy rękę.
def oblicz_sume(reka, wartosci_kart):
    if reduce(lambda acc, karta: acc + wartosci_kart[karta], reka, 0) > 21 and 11 in reka:
        reka.append(1)
    return reduce(lambda acc, karta: acc + wartosci_kart[karta], reka, 0)

#pytamy, czy gracz chce dobrac kartę.
def decyzja_gracza():
    return input("Czy chcesz dobrać kartę? (t/n): ").lower().startswith('t')

#pytamy, czy gracz chce zagrać ponownie.
def ponownie():
    return input("Czy chcesz zagrać ponownie? (t/n): ").lower().startswith('t')

#wywołujemy powyższe funkcje i rozpoczynamy rozgrywkę.
def graj():
    wartosci_kart = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10, 'A':11}
    talia = tasuj_talie()
    reka_gracza = rozdaj_karty(talia) 
    reka_krupiera = rozdaj_karty(talia) 
    
    while True:
        print(f"Twoje karty: {reprezentuj_reke(reka_gracza)} suma: {oblicz_sume(reka_gracza, wartosci_kart)}") 
        print(f"Karta krupiera: {reka_krupiera[0]}") 

        if oblicz_sume(reka_gracza, wartosci_kart) == 21: 
            print("Masz Blackjacka! Wygrywasz.")
            return
        if oblicz_sume(reka_gracza, wartosci_kart) > 21:
            print("Przekroczyłeś 21! Przegrywasz.")
            return
        if not decyzja_gracza(): 
            break

        reka_gracza.append(talia.pop()) 

    while oblicz_sume(reka_krupiera, wartosci_kart) < 17:
        reka_krupiera.append(talia.pop())

    print(f"Twoje karty: {reprezentuj_reke(reka_gracza)} suma: {oblicz_sume(reka_gracza, wartosci_kart)}") 
    print(f"Karty krupiera: {reprezentuj_reke(reka_krupiera)} suma: {oblicz_sume(reka_krupiera, wartosci_kart)}") 

    if oblicz_sume(reka_krupiera, wartosci_kart) > 21 or oblicz_sume(reka_gracza, wartosci_kart) > oblicz_sume(reka_krupiera, wartosci_kart):
        print("Gratulacje! Wygrałeś.")
    elif oblicz_sume(reka_gracza, wartosci_kart) == oblicz_sume(reka_krupiera, wartosci_kart):
        print("Remis!")
    else:
        print("Przegrałeś. Krupier wygrywa.")

#sprawdzamy, czy plik jest uruchamiany jako program główny, czy też jest importowany jako moduł do innego programu. 
if __name__ == "__main__": 
     while True:
        graj()
        if not ponownie():
           break
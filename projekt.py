#biblioteki użyte w programie: turtle-rysowanie, random-funkcja losująca liczby, mat-moduł matematyczny
import turtle
import random
import math

# Utworzenie okna dla rysowania
okno = turtle.Screen()
okno.setup(width=800, height=800)
okno.setworldcoordinates(-100, -100, 100, 100)
kursor = turtle.Turtle()
kursor.speed(20)

#inicjalizacja zmiennej jako promień okręgu
promien_okregu = 5

#Lista przechowująca informacje o okręgach
okregi = []

#funkcja wyswietlaaca aktualne położenie okręgów
def wyswietl_polozenie():
    for okrag in okregi:
        print(okrag)

# Funkcja do rysowania okręgów
def rysuj_okregi(ilosc_okregow):

    #Pętla iterująca po ilośći okręgów jako zadany parametr funkcji
    for nr_okregu in range(1, ilosc_okregow + 1):
        # Losowanie współrzędnych x i y
        x = random.randint(-100, 100)
        y = random.randint(-100, 100)

        # Przejście do losowej pozycji
        kursor.penup()
        kursor.goto(x, y)
        kursor.pendown()

        # Rysowanie okręgu o zadanym promieniu
        kursor.circle(promien_okregu)

        # Zapisanie informacji o okręgu w liście
        okreg = [nr_okregu, x, y, 5]
        okregi.append(okreg)

    #funkcja zwraca aktualną tablicę okręgów, informację o położeniu kursora oraz okno programu
    return okregi, kursor, okno

# Funkcja do przesunięcia określonego okręgu
def przesun_okrag(okregi, kursor, nr_okregu, przesuniecie_x, przesuniecie_y):
    # Wyszukanie okręgu z listy okręgów pod zadane kryterium jako numer okręgu
    for okrag in okregi:
        if okrag[0] == nr_okregu:
            # Aktualizacja współrzędnych okręgu
            okrag[1] += przesuniecie_x
            okrag[2] += przesuniecie_y

            # Przesunięcie okręgu w nowe miejsce bez rysowania na nowo
            kursor.penup()
            kursor.goto(okrag[1], okrag[2])
            kursor.pendown()
            kursor.circle(okrag[3])
            return
    
# Funkcja do sprawdzenia czy występuje kolizja pomiędzy dwoma okręgami
def czy_kolizja(okrag1, okrag2):
    odleglosc = math.sqrt((okrag1[1] - okrag2[1])**2 + (okrag1[2] - okrag2[2])**2)
    suma_promieni = okrag1[3] + okrag2[3]
    return odleglosc <= suma_promieni

# Funkcja do sprawdzenia kolizji między wszystkimi okręgami
def sprawdz_kolizje(okregi):
    for i in range(len(okregi)):
        for j in range(i + 1, len(okregi)):
            if czy_kolizja(okregi[i], okregi[j]):
                return True
    return False

# Rysowanie 20 okręgów i zapisanie ich informacji
okregi, kursor, okno = rysuj_okregi(20)
#wywołanie funcji - wyświetlenie położenia początkowego
wyswietl_polozenie()
print('-----------------')

#wywołanie funckji przesuwającej wybrany okrąg
przesun_okrag(okregi, kursor, 1, 20, 30)
#wywołanie funkcji - wyświetlenie położenia po przesunięciu
wyswietl_polozenie()
print('-----------------')


# Powiadomienie użytkownika o kolizji lub jej braku 
if sprawdz_kolizje(okregi):
    print("---KOLIZJA---")
else:
    print("---BRAK-KOLIZJI---")
    
#pętla rozuwająca okręgi między sobą jeśli (dopóki) są w kolizji między sobą
while sprawdz_kolizje(okregi):
    for okrag in okregi:
        # Losowanie współrzędnych x i y
        przesuniecie_x = random.randint(-100, 100)
        przesuniecie_y = random.randint(-100, 100)
        #wywołanie funkcji przesuwajacej okregi
        przesun_okrag(okregi, kursor, okrag[0], przesuniecie_x, przesuniecie_y)

# Zamknięcie okna po kliknięciu w nie
okno.exitonclick()

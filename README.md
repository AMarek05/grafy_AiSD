# grafy_AiSD
Zadanie 3: Algorytmy grafowe (python)
Program

Zaimplementuj algorytmy sortowania topologicznego wierzchołków grafu: (i) z wykorzystaniem trawersowania grafu w głąb (algorytm Tarjana) i ~~(ii) z usuwaniem wierzchołków niezależnych (algorytm Kahna)~~. Każdy z algorytmów należy zaimplementować na dwóch reprezentacjach maszynowych grafu: (a) macierz sąsiedztwa, (b) lista następników. Razem należy zaimplementować więc po 2 wersje każdego algorytmu: Tarjan_ms, Tarjan_ln, ~~Kahn_ms, Kahn_ln~~.
Algorytmy powinny wykrywać cykle w grafie wejściowym. W wersji przedstawianej na zaliczenie w przypadku znalezienia cyklu, należy przerwać sortowanie i wyświetlić komunikat informujący, że graf zawiera cykl i nie da się posortować topologicznie jego wierzchołków.
Program powinien umożliwiać wystartowanie algorytmu Tarjana z wierzchołka podanego przez użytkownika (ta wersja będzie wykorzystywana tylko podczas zaliczania programu na zajęciach) lub z wierzchołka domyślnego – o zerowym stopniu wejściowym (ta wersja będzie wykorzystywana do testów).
~~Program powinien wczytywać dane z pliku tekstowego, w którym pierwsza linia zawiera parę liczb określających liczbę wierzchołków (rząd grafu) i liczbę łuków (rozmiar grafu), a kolejne linie zawierają listę krawedzi, tj. pary wierzchołków połączonych łukiem. Spacja jest separatorem liczb w pojedynczej linii. Wierzchołki indeksujemy od 1.~~

Testy
Wygeneruj proste digrafy acykliczne o n wierzchołkach i współczynniku nasycenia krawędziami równym 50% dla 10-15 różnych wartości n z przedziału <100,k> (k należy je dobrać eksperymentalnie tak, aby możliwe było wykonanie pomiarów i aby jego wartość była możliwie duża; proponowane k=1500).
Zastosuj wszystkie algorytmy do posortowania wygenerowanych grafów. Zapisz czasy działania algorytmów.

Sprawozdanie
Wykonaj wykresy t=f(n) zależności czasu obliczeń t od liczby n wierzchołków w grafie (jeden wykres dla każdej reprezentacji maszynowej grafu). Na każdym wykresie przedstaw 2 krzywe – po jednej krzywej dla każdej metody sortowania topologicznego.
Wykonaj 2 wykresy w skali logarytmicznej (jeden wykres dla każdej metody sortowania topologicznego) t=f(n) zależności czasu obliczeń t od liczby n wierzchołków w grafie. Na każdym wykresie przedstaw po jednej krzywej dla każdej reprezentacji maszynowej grafu.
Opisz zalety i wady każdej reprezentacji grafu z punktu widzenia ich zastosowania w zaimplementowanych algorytmach.

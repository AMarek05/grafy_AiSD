class Graf:
    def __init__(self,V,E):
        self.V=V
        self.E=E

def graf_nieskierowany():
    m=0
    print("===WYBÓR METODY===")
    print("Podaj w jaki sposób zdefiniujesz graf(0-4):\n1. Macierz sąsiedztwa\n2. Macierz incydencji\n3. Lista krawędzi\n4. Lista sąsieztwa\n0. MENU")
    m=int(input())
    match(m):
        case 1:
            macierz_sąsiedztwa()

def graf_skierowany():
    m=0
    print("===WYBÓR METODY===")
    print("Podaj w jaki sposób zdefiniujesz graf(0-6):\n1. Macierz sąsiedztwa\n2. Macierz incydencji\n3. Lista krawędzi\n4. Lista następników\n5.Lista poprzedników\n6. Macierz grafu\n0. MENU")

def macierz_sąsiedztwa():
    return 9

def main():
    print("===MENU GŁÓWNE===")
    print("Podaj typ grafu (0-2):\n1. Nieskierowany\n2. Skierowany\n0. Wyjście")
    n=int(input())
    match(n):
        case 0:
            exit(0)
        case 1:
            graf_nieskierowany()
        case 2:
            graf_skierowany()
    V=[1,2,3,4,5]
    E=[1,2,3,4,5,6,7,8,9,10]
    g=Graf(V,E)


if __name__ == "__main__":
    main()
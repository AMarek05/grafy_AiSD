from collections import deque
import time
from sys import argv
from random import shuffle, sample


class Graf:
    def __init__(self,V,E):
        self.V=V
        self.E=E

def macierz_sąsiedztwa(wej):
    rząd=wej[0][0]
    macierz = [[0 for _ in range(rząd)] for _ in range(rząd)]
    wej.pop(0)
    for i in wej:
        macierz[i[0]-1][i[1]-1]=-1
        macierz[i[1]-1][i[0]-1]=1
    return macierz

def lista_następników(wej):
    macierz=[]
    rząd=wej[0][0]
    wej.pop(0)
    for _ in range (rząd):
        macierz.append([0])
    for i in wej:
        macierz[i[0]-1].append(i[1])
    licz=1
    for i in macierz:
        i.sort()
        i[0]=licz
        licz+=1
    return macierz

def alg_Kahna_ms(graf):
    poprzedniki=[]
    posortowane=[]
    visited=[]
    poprzedniki=[0 for _ in range(len(graf))]
    visited=[0 for _ in range(len(graf))]
    for i in range(len(graf)):
        for j in range(len(graf)):
            if graf[i][j]==1:
                poprzedniki[j]+=1
    queue=deque()
    for i in range(len(graf)):
        if poprzedniki[i]==0:
            queue.append(i)
            visited[i]=1
    while queue:
        elem=queue.popleft()
        posortowane.append(elem+1)
        for i in range(len(graf)):
            if graf[elem][i]==1:
                poprzedniki[i]-=1
        for i in range(len(graf)):
            if poprzedniki[i]==0 and visited[i]==0:
                queue.append(i)
                visited[i]=1
    posortowane.reverse()
    if len(posortowane)!=len(graf):
        print("Graf zawiera cykl, nie można go posortować")
        return
    else:
        return posortowane

def alg_Kahna_ln(graf):
    poprzedniki=[]
    posortowane=[]
    visited=[]
    poprzedniki=[0]*len(graf)
    visited=[0]*len(graf)
    for i in graf:
        for j in i[1:]:
            poprzedniki[j-1]+=1
    queue=deque()
    for i in range(len(graf)):
        if poprzedniki[i]==0:
            queue.append(i)
            visited[i]=1
    while queue:
        elem=queue.popleft()
        posortowane.append(elem+1)
        for i in graf[elem][1:]:
            poprzedniki[i-1]-=1
        for i in range(len(graf)):
            if poprzedniki[i]==0 and visited[i]==0:
                queue.append(i)
                visited[i]=1
    if len(posortowane)!=len(graf):
        print("Graf zawiera cykl, nie można go posortować")
        return
    else:
        return posortowane

def alg_Tarjana_ms(graf):
    kolor=[0]*len(graf) #0 - biały, 1 - szary, 2 - czarny
    posortowane=[]
    ścieżka=[]
    # print("===WYBÓR POCZĄTKU===")
    # print("Wybierz indeks początkowego wierzchołka:\n1. Najniższy indeks\n2. Indeks wpisany z klawiatury\n0. Wyjdź")
    # n=int(input("podaj liczbę (0-2): "))
    n = 1
    pocz = 1
    match(n):
        case 2:
            pocz=int(input("Podaj indeks początkowy: "))
        case 1:
            pocz=1
        case 0:
            exit(0)
    kolor[pocz-1]=1
    while len(posortowane)!=len(graf):
        czy_białe=False
        for i in range(len(graf[pocz-1])):
            if graf[pocz-1][i]==1 and kolor[i]==0:
                czy_białe=True
                ścieżka.append(pocz)
                pocz=i+1
                kolor[pocz-1]=1
                break
            if graf[pocz-1][i]==1 and kolor[i]==1:
                print("Graf zawiera cykl, nie można go posortować")
                return
        if not czy_białe:
            kolor[pocz-1]=2
            posortowane.append(pocz)
            if ścieżka:
                pocz=ścieżka.pop()
            else:
                czy_koniec=True
                for i in range(len(kolor)):
                    if kolor[i]!=2:
                        pocz=i+1
                        czy_koniec=False
                        break
                if czy_koniec==True:
                    break
    return posortowane

def alg_Tarjana_ln(graf):
    kolor=[0]*len(graf) #0 - biały, 1 - szary, 2 - czarny
    posortowane=[]
    ścieżka=[]
    # print("===WYBÓR POCZĄTKU===")
    # print("Wybierz indeks początkowego wierzchołka:\n1. Najniższy indeks\n2. Indeks wpisany z klawiatury\n0. Wyjdź")
    # n=int(input("podaj liczbę (0-2): "))
    n = 1
    pocz = 1
    match(n):
        case 2:
            pocz=int(input("Podaj indeks początkowy: "))
        case 1:
            pocz=1
        case 0:
            exit(0)
    kolor[pocz-1]=1
    while len(posortowane)!=len(graf):
        czy_białe=False
        for i in graf[pocz-1][1:]:
            if kolor[i-1]==0:
                czy_białe=True
                ścieżka.append(pocz)
                pocz=i
                kolor[pocz-1]=1
                break
            if kolor[i-1]==1:
                print("Graf zawiera cykl, nie można go posortować")
                return
        if not czy_białe:
            kolor[pocz-1]=2
            posortowane.append(pocz)
            if ścieżka:
                pocz=ścieżka.pop()
            else:
                czy_koniec=True
                for i in range(len(kolor)):
                    if kolor[i]!=2:
                        pocz=i+1
                        czy_koniec=False
                        break
                if czy_koniec==True:
                    break
    posortowane.reverse()
    return posortowane

def czy_posortowane(graf):
    print("Podaj ciąg do sprawdzenia:")
    T=list(map(int,input().split()))
    T2={}
    licz=0
    for i in T:
        licz+=1
        T2[i]=licz
    for i in range(len(graf)):
        for j in range(len(graf[i])):
            graf[i][j]=T2[graf[i][j]]
    for i in graf:
        for j in range(1,len(i)-1):
            if i[0]>=i[j]:
                print("nieposortowane")
                exit(0)
            else:
                continue
    print("posortowane")
    exit(0)
def dostępne_białe(kolor,graf,pocz):
    for i in graf[pocz-1][1:]:
        if kolor[i-1]==0:
            return True
    return False

def czy_spójne(kraw, n):
    adj=[[] for _ in range(n)]
    for u, v in kraw:
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)

    seen={0}
    queue=deque([0])
    while queue:
        x=queue.popleft()
        for y in adj[x]:
            if y not in seen:
                seen.add(y)
                queue.append(y)

    return len(seen) == n

def gen_nasycenie(n):
    topo=list(range(1, n+1))
    shuffle(topo)

    możliwe=[]
    for i in range(n):
        for j in range(i+1, n):
            możliwe.append((topo[i], topo[j]))

    max=len(możliwe)
    target=max//2

    while True:
        krawędzie=sample(możliwe,target)
        if czy_spójne(krawędzie, n):
            break

    inc=[]
    for u, v in krawędzie:
        inc.append([u, v])
    inc.sort()
    inc.insert(0, [n, len(krawędzie)])
    # print(*inc)
    return inc

def main():
    f=open("b.txt","r")
    wej=[]
    liczba_w = -1

    # Gdy podano 1 argument, interpretuj jako l. wierzchołków
    if len(argv) > 1:
        liczba_w = int(argv[1])
        assert liczba_w > 3 # Prowadzi do pętli nieskończonej jeśli 3 lub mniejsze
        wej=gen_nasycenie(liczba_w)
        if len(argv) == 4:
            # n = int(argv[2])
            n = 1 if argv[2] == "Matrix" else 2
            # m = int(argv[3])
            m = 1 if argv[3] == "Kahn" else 2
        else:
            n = 1
            m = 1
    else:
        for i in f:
            wej.append(list(map(int,i.split())))
        print("===WYBÓR METODY IMPLEMENTACJI===")
        print("Podaj w jaki sposób zdefiniujesz graf:\n1. Macierz sąsiedztwa\n2. Lista następników\n0. Wyjście")
        n=int(input("Liczba(0-2):"))

        print("===WYBÓR ALGORYTMU SORTOWANIA===")
        print("Podaj algorytm sortowania topologicznego:\n1. Algorytm Kahna\n2. Algorytm Tajrana\n0. Wyjście")
        m=int(input("Liczba(0-2):"))
    start = time.time()
    out = "Dla "
    match(n):
        case 0:
            exit(0)
        case 1:
            graf=macierz_sąsiedztwa(wej)
            out += "macierzy sąsiedztwa algorytmem "
            match(m):
                case 1:
                    posortowane=alg_Kahna_ms(graf)
                    out += "Kahna "
                    # print(posortowane)
                case 2:
                    posortowane=alg_Tarjana_ms(graf)
                    out += "Tarjana"
                    # print(posortowane)
        case 2:
            graf=lista_następników(wej)
            out += "listy następników algorytmem "
            match(m):
                case 1:
                    posortowane=alg_Kahna_ln(graf)
                    out += "Kahna "
                    # print(posortowane)
                case 2:
                    posortowane=alg_Tarjana_ln(graf)
                    out += "Tarjana"
                    # print(posortowane)
    end = time.time()
    exec_time = (end - start) * 1000
    print(f"{liczba_w};{exec_time:.3f}")
    f.close()
if __name__ == "__main__":
    main()


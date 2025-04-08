class Graf:
    def __init__(self,V,E):
        self.V=V
        self.E=E

def macierz_sąsiedztwa(wej):
    rząd=wej[0][0]
    rozmiar=wej[0][1]
    macierz = [[0 for i in range(rząd)] for j in range(rząd)]
    wej.pop(0)
    for i in wej:
        macierz[i[0]-1][i[1]-1]=1
        macierz[i[1]-1][i[0]-1]=-1
    return macierz

def lista_następników(wej):
    macierz=[]
    rząd=wej[0][0]
    rozmiar=wej[0][1]
    wej.pop(0)
    for i in range (rząd):
        macierz.append([0])
    for i in wej:
        macierz[i[0]-1].append(i[1])
    licz=1
    for i in macierz:
        i.sort()
        i[0]=licz
        licz+=1
    return macierz

def main():
    f=open("wej.txt","r")
    wej=[]
    for i in f:
        wej.append(list(map(int,i.split())))
    print(wej)
    print("===WYBÓR METODY===")
    print("Podaj w jaki sposób zdefiniujesz graf:\n1. Macierz sąsiedztwa\n2. Lista następników\n0. Wyjście")
    n=int(input("Liczba(0-2):"))
    match(n):
        case 0:
            exit(0)
        case 1:
            graf=macierz_sąsiedztwa(wej)
        case 2:
            graf=lista_następników(wej)

if __name__ == "__main__":
    main()
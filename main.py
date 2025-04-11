from collections import deque


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
        macierz[i[0]-1][i[1]-1]=-1
        macierz[i[1]-1][i[0]-1]=1
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

# def alg_Kahna_ms(graf):
#     poprzedniki={}
#     posortowane=[]
#     for i in range(len(graf)):
#         poprzedniki[i+1]=[]
#         for j in range(len(graf[i])):
#             if graf[i][j]==-1:
#                 poprzedniki[i+1].append(j+1)
#     pętla=False
#     while len(posortowane)<len(graf):
#         if pętla:
#             print("Graf zawiera cykl, nie można go posortować")
#             break
#         else:
#             pętla=True
#         for i in range(1,len(graf)+1):
#             if i in poprzedniki.keys():
#                 if len(poprzedniki[i])==0:
#                     pętla=False
#                     posortowane.append(i)
#                     for j in range(1,len(graf)+1):
#                         if j in poprzedniki.keys():
#                             if i in poprzedniki[j] :
#                                 poprzedniki[j].remove(i)
#                     poprzedniki.pop(i)
#                     break
#     posortowane.reverse()
#     return posortowane

def alg_Kahna_ms(graf):
    poprzedniki=[]
    posortowane=[]
    visited=[]
    poprzedniki=[0 for i in range(len(graf))]
    visited=[0 for i in range(len(graf))]
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
        return posortowane
    else:
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

def main():
    f=open("wej2.txt","r")
    wej=[]
    for i in f:
        wej.append(list(map(int,i.split())))
    print(wej)
    print("===WYBÓR METODY IMPLEMENTACJI===")
    print("Podaj w jaki sposób zdefiniujesz graf:\n1. Macierz sąsiedztwa\n2. Lista następników\n0. Wyjście")
    n=int(input("Liczba(0-2):"))
    print("===WYBÓR ALGORYTMU SORTOWANIA===")
    print("Podaj algorytm sortowania topologicznego:\n1. Algorytm Kahna\n2. Algorytm Tajrana\n0. Wyjście")
    m=int(input("Liczba(0-2):"))
    match(n):
        case 0:
            exit(0)
        case 1:
            graf=macierz_sąsiedztwa(wej)
            match(m):
                case 1:
                    posortowane=alg_Kahna_ms(graf)
                    print(posortowane)
        case 2:
            graf=lista_następników(wej)
            print(graf)
if __name__ == "__main__":
    main()
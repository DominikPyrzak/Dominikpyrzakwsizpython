liczbaG=int(input("Podaj liczbę gwiazdek w lini: "))

for i in range(liczbaG):
    for j in range(i+1):
        print("*", end=" ")
    print("")

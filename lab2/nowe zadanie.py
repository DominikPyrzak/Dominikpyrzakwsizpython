n=int(input("Ile elementów wpisać?: "))
a=int(input("Podaj pierwszy wyraz ciągu: "))
r=int(input("Podaj różnice ciągu: "))

#wersja ze wzorem
# an=a+(n-1)+r
#w=0
#for i in range(1, n+1):
#    w=a+(i-1)*r
#    print(w)


#wersja2
if r!=0:
    if r>0:
        k=a+(n-1)*r+1
    else:
        k=a+(n-1)*r-1
    for i in range(a, k, r):
        print(i)
else:
    print("Ciąg jest stały - jego różnica wynosi 0")
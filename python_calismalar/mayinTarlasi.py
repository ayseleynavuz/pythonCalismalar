print("---Mayın Tarlası Oyunu---")
import random
w,h=10,10
matrix=[[0 for x in range(w)] for y in range(h)]
print(matrix)

for i in range(10):
    i=random.randint(0,9)
    j=random.randint(0,9)
    matrix[i][j]=1
print(matrix)

deger = False
toplam=0
while deger==False:
    sutun=int(input("sütun giriniz: "))
    satir=int(input("satır giriniz: "))
    if matrix[satir][sutun]==0:
        toplam=toplam+1
        print(toplam)
    else:
        print("oyun bitti.")   
        print(toplam)
        deger=True




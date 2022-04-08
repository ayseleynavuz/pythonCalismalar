#Kullanıcının girdiği m x n boyutunda rastgele sayılarla doldurulmuş matris oluşturulup bu matrisin transpozesini bulunuz.
import random

satirSayisi=int(input("satır sayisini giriniz: "))
sutunSayisi=int(input("sütun sayisini giriniz: "))

matris=[[0 for x in range(sutunSayisi)] for y in range(satirSayisi)]#m x n
matrisTranspoze=[[0 for x in range(satirSayisi)] for y in range(sutunSayisi)]#n x m
for i in range(satirSayisi):
  for j in range(sutunSayisi):
    matris[i][j] = random.randint(0,9)
    matrisTranspoze[j][i] = matris[i][j] #transpozesini oluşturma işlemi

print(matris)
print(matrisTranspoze)





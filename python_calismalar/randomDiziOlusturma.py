#Random sayı üreterek dizi oluşturmak
#kullanıcının istediği büyüklükte bir dizi oluşturup,0-100 arasında random sayılarla doldurulacak ve standart sapması hesaplanacak.
import random
import math

uzunluk=int(input("dizi uzunluğunu giriniz: "))
dizi= []
for i in range(uzunluk):
  dizi.append(random.randint(0,100))
print(dizi)

toplam=0
for x in dizi:
  toplam+=x
ortalama=toplam/uzunluk
#standart sapma hesabı
farkToplam=0
for x in dizi:
  fark=x-ortalama
  fark =fark**2 #fark değişkeninin karesi alınır
  farkToplam+=fark
standartSapma=math.sqrt(farkToplam/uzunluk)
print("Standart sapma: ",standartSapma)

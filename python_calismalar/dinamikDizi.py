#Dinamik dizi kullanımı
#kullanıcıdan istediği kadar sayıyı alarak diziye aktaran bu sayıların toplamını ve ortalamasını bulan programı yazınız.

adet=int(input("kaç adet sayı girmek istiyorsunuz: "))
dizi=[] #boş bir dizi tanımladık
for i in range(adet):
  dizi.append(int(input("sayıyı giriniz: "))) #girilen her sayı append komutu ile diziye aktarılır
print(dizi)  

toplam=0
for x in dizi:
  toplam+=x
print("Toplam: ", toplam)
print("Ortalama: ", toplam/adet)



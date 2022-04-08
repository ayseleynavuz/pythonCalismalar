#basit bir hesap makinesi uygulaması

def Topla(sayi1,sayi2):
  return sayi1+sayi2
def Cikar(sayi1,sayi2):
  return sayi1-sayi2
def Carp(sayi1,sayi2):
  return sayi1*sayi2
def Bol(sayi1,sayi2):
  return sayi1/sayi2

print("iŞLEMLER: \n1-Topla\n2-Çıkar\n3-Çarp\n4-Böl ")
islem= input("İŞLEM SEÇİNİZ: ")
sayi1= int(input("Birinci sayiyi giriniz: "))
sayi2= int(input("İkinci sayiyi giriniz: "))

if islem=='1':
  print("Toplam: "+str(Topla(sayi1,sayi2)))
elif islem == '2':
  print("Sonuç: "+str(Cikar(sayi1,sayi2)))
elif islem == '3':
  print("Sonuç: "+str(Carp(sayi1,sayi2)))
elif islem == '4':
  print("Sonuç: "+str(Bol(sayi1,sayi2)))
else:
  print("lütfen 1-4 arasında işlem seçiniz.")


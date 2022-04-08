#kullanıcıdan alınan bir kelimede kaç adet harf ve kelime olduğunu bulan programı yazınız.
metin = input("bir string,metin giriniz: ")
boslukSayac=0
for karakter in metin:
  if karakter == " ": #karakter boşluğa eşitse sayacı bir arttır
    boslukSayac+=1
print("boşluk adedi: ",boslukSayac)
print("kelime sayısı: ",boslukSayac+1)    
print("harf sayısı: ",len(metin))




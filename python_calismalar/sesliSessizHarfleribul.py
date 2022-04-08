#kullanicidan metin alarak içindeki sesli ve sessiz harfleri bulan programı yazınız.

yazi=input("bir metin giriniz: ")
sesli="aeıioöuü"
sesliSayac=0
for harf in yazi:
  if harf in sesli:
    sesliSayac+=1
print("sesli harf sayısı: ",sesliSayac)
print("sessiz harf sayısı: ",len(yazi)-sesliSayac)
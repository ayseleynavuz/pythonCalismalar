#Insertion Sort (Seçme Sıralama): bir key seçimi yapılır o seçilen key solundaki sayılarla karşılaştırılıyor
# büyük olan sayılar sağa kaydırılıyor

def insertion_sort(dizi):
    for i in range(1,len(dizi)):   #döngü 1'den başlıyor 0.sıradaki sayıyı sıralı kabul ediyoruz
        key = dizi[i]
        j = i-1
        while j >=0 and key < dizi[j]:
            dizi[j+1] = dizi[j]  #sağa kaydırma yapmak için
            j = j-1
        dizi[j+1] = key    
    
    
sirasizDizi=[3,10,-2,-1,15,400,17]   
insertion_sort(sirasizDizi)           
print(sirasizDizi)
    
    

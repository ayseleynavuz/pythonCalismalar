#selection sort dizini tüm elemanlarını dolaşır en küçüğü bulur
def selection_sort(dizi):
    for i in range(len(dizi)):             #dizinin tüm elemanlarını dolaşan bir döngü
        min_index = i                      #üzerinde bulunduğu indisi min kabul edecek
        for j in range(i+1,len(dizi)):     #devamlı sağa doğru kaydığı için i+1 'den başlatıyoruz
            if dizi[min_index] > dizi[j]:  #dizinin min indexi üzerinde bulunduğu sayıdan büyükse
                min_index = j              #min indexi güncelle   
        if min_index != i:
            dizi[min_index],dizi[i] = dizi[i],dizi[min_index] #swap işlemi yapılıyor

sirasizDizi=[3,10,-2,-1,15,400,17]   
selection_sort(sirasizDizi)           
print(sirasizDizi)

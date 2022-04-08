#merge sort da küçük diziler birleştirilip büyük dizi oluşturulur
def merge(dizi):
    if len(dizi) > 1:
        print("Parçalanan değerler "+ str(dizi))
        orta = len(dizi)//2
        solDizi= dizi[:orta]  #başlangıç 0 dan ortaya kadar alıyor,orta dahil değil
        sagDizi= dizi[orta:]    #ortadan başlar orta dahil geri kalanını diziye aktarır
        merge(sagDizi)          #recursive olarak geri çağrılır,tek eleman kalana kadar
        merge(solDizi)
        mergeSort(dizi,solDizi,sagDizi)
        
def mergeSort(dizi,solDizi,sagDizi): 
       i=0
       j=0
       k=0
       
       while i < len(solDizi) and j < len(sagDizi):
           if solDizi[i] < sagDizi[j]:
               dizi[k] = solDizi[i]
               i+=1
           else:
               dizi[k] = sagDizi[j]
               j+=1
           k+=1
            
       while i < len(solDizi):
            dizi[k] = solDizi[i]
            i+=1
            k+=1
       while i < len(sagDizi):
            dizi[k] = sagDizi[i]
            j+=1
            k+=1    
       print("Birleştirimiş dizi "+ str(dizi))
        
                  
sirasizDizi=[3,10,-2,-1,15,400,17]   
merge(sirasizDizi)           
print(sirasizDizi)                  
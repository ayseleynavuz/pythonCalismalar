def buble_sort(dizi):
    for i in range(len(dizi)-1):
        for j in range(len(dizi)-1-i):  #en büyük eleman en sona geçer
            if dizi[j] > dizi[j+1]:
                dizi[j],dizi[j+1] = dizi[j+1],dizi[j]
                
sirasizDizi=[3,10,-2,-1,15,400,17]   
buble_sort(sirasizDizi)     
print(sirasizDizi)      
  
             
            
        
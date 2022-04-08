#YILDIZLARLA ŞEKİL ÇİZDİRME ÖRNEK SORULAR
print("1.soru \n")
#****
#****
#****
#****
     
satir_sayisi = 4
sutun_sayisi = 4
for satir in range(satir_sayisi):
    for sutun in range(sutun_sayisi):
        print("*" , end=' ')
    print()
       
           
print("2.soru \n")
#*
#**
#***
#****

satir_sayisi = 4
for satir in range(1,satir_sayisi+1):
    yildiz_sayisi = satir
    for i in range(yildiz_sayisi):  #print("*" *yildiz_sayisi) tek satır kodla aynı çıktıyı verir
        print("*" , end=' ')
    print()
    
print("3.soru \n")
#   *
#  **
# ***
#****
satir_sayisi = 4
sutun_sayisi = 4
for satir in range(1,satir_sayisi+1):
    bosluk_sayisi = satir_sayisi - satir
    yildiz_sayisi = sutun_sayisi - bosluk_sayisi
    
    for bosluk in range(bosluk_sayisi):
        print(" " , end=' ')
    for yildiz in range(yildiz_sayisi):
        print("*" , end=' ')  
    print()
    
print("4.soru \n")  #yıldız sayisi = satir sayisi + 1 - kaçıncı satır
#****
#***
#**
#*
satir_sayisi = 4
sutun_sayisi = 4
for satir in range(1,satir_sayisi+1):
    yildiz_sayisi = satir_sayisi + 1 - satir
    
    for yildiz in range(yildiz_sayisi):
        print("*" , end=' ')  
    print()
    
#yukarıdaki ile aynı çıktıyı verecektir        
for yildiz_sayisi in range(satir_sayisi,0,-1):
    for yildiz in range(yildiz_sayisi):
        print("*" , end=' ')  
    print()
        
    
print("5.soru \n")
#*
#**
#***
#****
#*****
#****
#***
#**
#*

satir_sayisi = 4
sutun_sayisi = 4
for satir in range(1,satir_sayisi+1):
    for yildiz in range(satir):
        print("*", end='')
    print()
    
satir_sayisi = 5
sutun_sayisi = 5

for yildiz_sayisi in range(satir_sayisi,0,-1):
    for yildiz in range(yildiz_sayisi):
        print("*", end='')
    print()
        
         
    
        
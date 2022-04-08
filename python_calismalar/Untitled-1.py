
girilenSayi=int(input("bir sayi giriniz:"))
sayac=2
asal_sayılar=[]
while girilenSayi >0:
    asal_sayılar.append(girilenSayi)
    while sayac<girilenSayi:
        if girilenSayi%sayac==0:
            asal_sayılar.remove(girilenSayi)
            break
        sayac+=1

    sayac=2
    girilenSayi-=1

print(asal_sayılar)


'''
def asal_Mi (sayi):
    for i in range(2,sayi):
        if sayi%i==0:
            return False
    return True

sayi=int(input("sayi giriniz: "))
asal_sayılar=[]

for i in range(2,sayi+1):
    if asal_Mi(i):
        asal_sayılar.append(i)

print(asal_sayılar)
'''

'''

print("-----girilen sayının faktoriyelini bulma----")
sayi=int(input("sayi giriniz: "))

faktoriyel=1
for i in range(1,sayi+1):
    faktoriyel=faktoriyel*i

print("{}!".format(sayi) + faktoriyel)

print("---------")

'''

sahipOlunanPara=2000

secim=input("Kartı yerlestirmek için 's' ayrılmak için 'a' yazınız.")

if secim == "s":
    print("atmye giriş yaptınız.")
    while True:
         islem=int(input(print("Bir işlem seçiniz: \n1-Para Çekme\n2-Para Yatırma\n3-Kart Bilgileri\n4-Kart İade")))
         if islem==1:
             cekilecekPara=int(input("Çekmek istediğiniz para değerini giriniz: "))
             if sahipOlunanPara<cekilecekPara:
                 print("bu işlem için yeterli bakiyeniz bulunmamaktadır.")
             else:
                 sahipOlunanPara -= cekilecekPara
                 print("hesabınızda kalan para: ",sahipOlunanPara)
                 
         if islem==2:
             yatırılacakPara=int(input("Yatırmak istediğiniz para değerini giriniz: "))
             sahipOlunanPara=sahipOlunanPara+yatırılacakPara
             print("hesabınızda kalan para: ",sahipOlunanPara)
    
         if islem==3:
             print("Kişinin kart bilgileri:\nad:.......\nsoyad:.....\niban-no:......\nkart-no:......\n")
    
    
         if islem==4:
             print("Kart iadesi istendi")
             break
else:
    print("atmden ayrıldınız...")











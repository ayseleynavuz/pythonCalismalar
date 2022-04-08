#kullanıcıdan alınan 4 basamaklı bir sayıyı yazıyla ekrana yazınız.
birler=["","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]
onlar=["","on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]
yuzler=["","yüz","ikiyüz","üçyüz","dörtyüz","beşyüz","altıyüz","yediyüz","sekizyyüz","dokuzyüz"]
binler=["","bin","ikibin","üçbin","dörtbin","beşbin","altıbin","yedibin","sekizbin","dokuzbin"]

sayi=int(input("dört basamaklı bir sayı giriniz: "))
s = str(sayi) #girilen 4 basamaklı sayı string haline getirilir
print(binler[int(s[0])],yuzler[int(s[1])],onlar[int(s[2])],birler[int(s[3])])



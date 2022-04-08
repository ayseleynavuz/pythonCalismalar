#0-1000 arasındaki asal sayıları bulan programı yazınız
bolenSayac=0

for j in range(3,1000):
  bolenSayac=0
  for i in range(2,j):
    if (j%i == 0) :
      bolenSayac+=1
  if bolenSayac==0:
    print(j)
    
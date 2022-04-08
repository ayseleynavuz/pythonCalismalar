#matris toplama
#rastgele sayılardan 3x3 matris oluşturup, toplamını hesaplayan programı yazınız
import random
m1=[[0 for x in range(3)] for y in range(3)] # 3x3'lük boş matris oluşturulması işlemi
m2=[[0 for x in range(3)] for y in range(3)]
mt=[[0 for x in range(3)] for y in range(3)]

for i in range(3):
  for j in range(3):
    m1[i][j] = random.randint(0,5)
    m2[i][j] = random.randint(0,5)
    mt[i][j] = m1[i][j] + m2[i][j]
print(mt)

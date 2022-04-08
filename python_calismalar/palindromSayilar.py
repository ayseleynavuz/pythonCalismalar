#1000-100000 arasındaki palindrom sayıları bulan programı yazınız
for i in range(1000,100000):
  s = str(i)
  t = s[::-1] #tersine çevirme 
  if s == t:
    print(s)
    

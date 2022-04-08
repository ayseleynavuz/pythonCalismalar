import random
def squid():
    w=18
    h=2
    matris=[[0 for x in range(h)] for y in range(w)]
    print(matris)
    for i in range(w):
            stepFail=random.randint(0,1)
            matris[i][stepFail]=1

    print(matris)
    counter=0
    while counter<w:
        print(counter+1," .seçim:")
        secim=int(input())
        if matris[counter][secim]==1:
            print("oyunu kaybettiniz.")
            break
        else:
            print("sonraki ele geçtiniz.")
            counter+=1

squid()



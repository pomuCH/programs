n =5487962238152
lis=[]

for i in range(2,n+1):
    while True:
        if n%i == 0 and n!=1:
            lis.append(i) # 余り0なら素因数分解リストにappendする
            n = n//i # nの更新
            print(lis)
            print("n={}".format(n)) # nの更新状況をみてみる
        elif n==1:
            break
        else:
            break

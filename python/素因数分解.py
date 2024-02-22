n = 30011
s=[]

for i in range(2,n+1):
  while True:
    if n%i == 0 and n!=1:
      s.append(i)
      n = n//i
      print(s)
      print("n={}".format(n))
    elif n==1:
      break
    else:
      break

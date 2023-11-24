a=list(map(int, input().split()))
n=len(a)
for i in range(0,n-1):
	for j in range(i+1,n):
		if a[i]>a[j]:
			x=a[i]
			y=a[j]
			a[i]=y
			a[j]=x
print(a)

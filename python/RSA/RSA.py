#codeing : utf-8
import random

def gcd(a, b): #gcd = greatest common divisor (最大公約数)
  while b:
    a, b = b, a % b #ユークリッドの互除法
  return a

def tagainiso(num):
  totient =[]
  for i in range (1,num+1):
    if gcd(num,i)==1:
      totient.append(i)
    if i>100:
      break
  return totient

def lcm(a,b): #最小公倍数 (lcm) = a*b/最大公約数 (gcd)
  return a * b / gcd(a,b)

def encode(m): #暗号化
  mm=list(m.encode("utf8"))
  integer=mm
  #print(f'UNコード化={integer}')
  for i in range(0,int(len(integer))):
    c.append((integer[i]**k_1)%n)


## ax - by = 1 の整数解x,yを求める。
def d_cal(a,b):

    # a>bの関係にしておく
    a,b = (b,a) if abs(a)<abs(b) else (abs(a),abs(b))

    pre_x, now_x = 0,1     # xの値は、最初は商x(-1)
    pre_y, now_y = 1,0     # yの値は、最初は1

    while True:
        # 商
        q = a//b

        # 「前々回の係数合計 - 前回の係数合計に商をかけた値」が今回の係数合計になる。
        pre_x, now_x = now_x, pre_x + now_x * q
        pre_y, now_y = now_y, pre_y  + now_y * q

        if a%b == 1:    # 余りが1でループを抜け終了
            break
        elif a%b == 0:  # 余りが1になる前に0になってしまった場合
            print('aとbは互いに素ではないので、不定方程式ax+by=1を満たす整数x,yは存在しません。')
            return None, None

        # 割られる数, 割る数 = 割る数, 余り
        a, b = b, a%b
    return now_x, now_y

def adjust(a,b):
  i=0
  while True:
    x=(p-1)*(q-1)*i-a
    y=k_1*i-b
    if (k_1*x-(p-1)*(q-1)*y)==1 and x>0:
      #print("yes yes yes")
      break
    i+=1
  return x, y

j=1
i=1
p=101  #p<q
q=307
n=p*q
e=tagainiso((p-1)*(q-1))
k_1=e[random.randint(1,int(len(e))-1)]
# ex -  Ly = 1

a = k_1
b = (p-1)*(q-1)
xx,y = d_cal(a,b)
if (a*xx-b*y)==-1:
  xxx,yy=adjust(xx,y)
else:
  xxx,yy=xx,y
print(f"params:p = {p} , q = {q} , n = {n} ,  e = {k_1} , L = {(p-1)*(q-1)} , d = {xxx} , y  = {yy}")
print(f"公開鍵 = {n} , {k_1}")
k_2=xxx
m=str(input('入力 >>> '))
integer = []
c=[]
encode(m)
print(f'暗号文 = {c}')

###複合
x=[0]*len(c)
for i in range(0,int(len(c))):
    x[i]=(c[i]**k_2)%n
result = bytes(x).decode("utf8")
print(f'復号文 = {result}')

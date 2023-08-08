import tkinter as tk
import requests
from PIL import Image
from PIL import ImageDraw
import socket
win= tk.Tk()
win.geometry('2000x1000')
win.configure(bg='white')
win.title('寿司注文')

ip1 = 'ここにはラインに送信されたipを入力してください'

port1 = 8765
server = (ip1, port1)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(server)

#画像処理
url = 'https://www.kaitenmaru.com/fcontents/images/original/menu_master/20/%E7%94%9F%E3%81%A8%E3%82%8D%E3%82%AD%E3%83%B3%E3%82%B0%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3.jpg'
r = requests.get(url)
if r.status_code == 200:
    with open('サーモン.jpg', 'wb') as f:
        f.write(r.content)
#jpgからpng--------------------------------------
im = Image.open("サーモン.jpg")
im.save('サーモン.png')
im.save('サーモン.png')
#円形に切り抜く-----------------------------------
path = "サーモン.png"
offset = 80     
img = Image.open(path)
mask = Image.new("L", img.size)
draw = ImageDraw.Draw(mask)
draw.ellipse([(offset, offset), (img.size[0] - offset, img.size[1] - offset)], 255)
del draw
img.putalpha(mask)
img.save("サーモン.png")
#画像の大きさ変更-----------------------------------

img1= Image.open('サーモン.png')
img_resize = img1.resize((197,200))
img_resize.save('サーモン.png')
#--------------------------------------------------
img2=tk.PhotoImage(file="サーモン.png",width=190,height=190)
lbl = tk.Label(text='サーモン',font=("MSゴシック","20","bold"))
lbl.configure(bg='white')
lbl.place(x=250, y=30)
#画像処理
url = 'https://s3-ap-northeast-1.amazonaws.com/ledge-ai-assets/media/wp-content/uploads/2020/11/06164745/main24.png'
r = requests.get(url)
if r.status_code == 200:
    with open('マグロ.jpg', 'wb') as f:
        f.write(r.content)
#jpgからpng--------------------------------------
im = Image.open("マグロ.jpg")
im.save('マグロ.png')
im.save('マグロ.png')
#円形に切り抜く-----------------------------------
path = "マグロ.png"
offset = 80     
img = Image.open(path)
mask = Image.new("L", img.size)
draw = ImageDraw.Draw(mask)
draw.ellipse([(offset, offset), (img.size[0] - offset, img.size[1] - offset)], 255)
del draw
img.putalpha(mask)
img.save("マグロ.png")
#画像の大きさ変更-----------------------------------

img3= Image.open('マグロ.png')
img_resize = img3.resize((187,190))
img_resize.save('マグロ.png')
#--------------------------------------------------
img4=tk.PhotoImage(file="マグロ.png",width=190,height=190)
lbl = tk.Label(text='マグロ',font=("MSゴシック","20","bold"))
lbl.configure(bg='white')
lbl.place(x=1900, y=30)
#画像処理
url = 'https://cdnyshopping.buyee.jp/i/l/keishin_na-susi-tako'
r = requests.get(url)
if r.status_code == 200:
    with open('タコ.jpg', 'wb') as f:
        f.write(r.content)
#jpgからpng--------------------------------------
im = Image.open("タコ.jpg")
im.save('タコ.png')
im.save('タコ.png')
#円形に切り抜く-----------------------------------
path = "タコ.png"
offset = 80     
img = Image.open(path)
mask = Image.new("L", img.size)
draw = ImageDraw.Draw(mask)
draw.ellipse([(offset, offset), (img.size[0] - offset, img.size[1] - offset)], 255)
del draw
img.putalpha(mask)
img.save("タコ.png")
#画像の大きさ変更-----------------------------------

img5= Image.open('タコ.png')
img_resize = img5.resize((197,200))
img_resize.save('タコ.png')
#--------------------------------------------------
img6=tk.PhotoImage(file="タコ.png",width=190,height=190)
lbl = tk.Label(text='タコ',font=("MSゴシック","20","bold"))
lbl.configure(bg='white')
lbl.place(x=250, y=600)
#画像処理
url = 'https://prtimes.jp/i/1312/93/resize/d1312-93-755663-0.jpg'
r = requests.get(url)
if r.status_code == 200:
    with open('エビ.jpg', 'wb') as f:
        f.write(r.content)
#jpgからpng--------------------------------------
im = Image.open("エビ.jpg")
im.save('エビ.png')
im.save('エビ.png')
#円形に切り抜く-----------------------------------
path = "エビ.png"
offset = 80     
img = Image.open(path)
mask = Image.new("L", img.size)
draw = ImageDraw.Draw(mask)
draw.ellipse([(offset, offset), (img.size[0] - offset, img.size[1] - offset)], 255)
del draw
img.putalpha(mask)
img.save("エビ.png")
#画像の大きさ変更-----------------------------------

img7= Image.open('エビ.png')
img_resize = img7.resize((197,200))
img_resize.save('エビ.png')
#--------------------------------------------------
img8=tk.PhotoImage(file="エビ.png",width=190,height=190)
lbl = tk.Label(text='エビ',font=("MSゴシック","20","bold"))
lbl.configure(bg='white')
lbl.place(x=1100, y=30)
#画像処理
url = 'https://tsurinews.jp/data/wp-content/uploads/2020/11/202011kura_02.jpg'
r = requests.get(url)
if r.status_code == 200:
    with open('カンパチ.jpg', 'wb') as f:
        f.write(r.content)
#jpgからpng--------------------------------------
im = Image.open("カンパチ.jpg")
im.save('カンパチ.png')
im.save('カンパチ.png')
#円形に切り抜く-----------------------------------
path = "カンパチ.png"
offset = 80     
img = Image.open(path)
mask = Image.new("L", img.size)
draw = ImageDraw.Draw(mask)
draw.ellipse([(offset, offset), (img.size[0] - offset, img.size[1] - offset)], 255)
del draw
img.putalpha(mask)
img.save("カンパチ.png")
#画像の大きさ変更-----------------------------------
from PIL import Image
img9= Image.open('カンパチ.png')
img_resize = img9.resize((197,200))
img_resize.save('カンパチ.png')
#--------------------------------------------------
img10=tk.PhotoImage(file="カンパチ.png",width=190,height=190)
lbl = tk.Label(text='カンパチ',font=("MSゴシック","20","bold"))
lbl.configure(bg='white')
lbl.place(x=1100, y=600)
#画像処理
url='https://kyodonewsprwire.jp/prwfile/release/M102330/202004078860/_prw_PI6im_SVhSAFOI.jpg'
r = requests.get(url)
if r.status_code == 200:
    with open('タイ.jpg', 'wb') as f:
        f.write(r.content)
#jpgからpng--------------------------------------
im = Image.open("タイ.jpg")
im.save('タイ.png')
im.save('タイ.png')
#円形に切り抜く-----------------------------------
path = "タイ.png"
offset = 80     
img = Image.open(path)
mask = Image.new("L", img.size)
draw = ImageDraw.Draw(mask)
draw.ellipse([(offset, offset), (img.size[0] - offset, img.size[1] - offset)], 255)
del draw
img.putalpha(mask)
img.save("タイ.png")
#画像の大きさ変更-----------------------------------

img11= Image.open('タイ.png')
img_resize = img11.resize((197,200))
img_resize.save('タイ.png')
#--------------------------------------------------
img12=tk.PhotoImage(file="タイ.png",width=190,height=190)
lbl = tk.Label(text='タイ',font=("MSゴシック","20","bold"))
lbl.configure(bg='white')
lbl.place(x=1900, y=600)
#画像処理
url='https://ascii.jp/img/2019/09/03/1541718/o/a4c98860e4416599.jpg'
r = requests.get(url)
if r.status_code == 200:
    with open('いくら.jpg', 'wb') as f:
        f.write(r.content)
#jpgからpng--------------------------------------
im = Image.open("いくら.jpg")
im.save('いくら.png')
im.save('いくら.png')
#円形に切り抜く-----------------------------------
path = "いくら.png"
offset = 80     
img = Image.open(path)
mask = Image.new("L", img.size)
draw = ImageDraw.Draw(mask)
draw.ellipse([(offset, offset), (img.size[0] - offset, img.size[1] - offset)], 255)
del draw
img.putalpha(mask)
img.save("いくら.png")
#画像の大きさ変更-----------------------------------

img13= Image.open('いくら.png')
img_resize = img13.resize((197,200))
img_resize.save('いくら.png')
#--------------------------------------------------
img14=tk.PhotoImage(file="いくら.png",width=190,height=190)
lbl = tk.Label(text='いくら',font=("MSゴシック","20","bold"))
lbl.configure(bg='white')
lbl.place(x=250, y=400)
#画像処理
url='https://cdn.goope.jp/160597/200426124648-5ea504281a6fe.png'
r = requests.get(url)
if r.status_code == 200:
    with open('太刀魚.jpg', 'wb') as f:
        f.write(r.content)
#jpgからpng--------------------------------------
im = Image.open("太刀魚.jpg")
im.save('太刀魚.png')
im.save('太刀魚.png')
#円形に切り抜く-----------------------------------
path = "太刀魚.png"
offset = 80     
img = Image.open(path)
mask = Image.new("L", img.size)
draw = ImageDraw.Draw(mask)
draw.ellipse([(offset, offset), (img.size[0] - offset, img.size[1] - offset)], 255)
del draw
img.putalpha(mask)
img.save("太刀魚.png")
#画像の大きさ変更-----------------------------------

img15= Image.open('太刀魚.png')
img_resize = img15.resize((197,200))
img_resize.save('太刀魚.png')
#--------------------------------------------------
img16=tk.PhotoImage(file="太刀魚.png",width=190,height=190)
lbl = tk.Label(text='太刀魚',font=("MSゴシック","20","bold"))
lbl.configure(bg='white')
lbl.place(x=2100, y=400)
def orders(event):
    s.send(b'1')
def orderm(event):
    s.send(b'2')
def ordert(event):
    s.send(b'3')
def ordere(event):
    s.send(b'4')
def orderk(event):
    s.send(b'5')
def orderb(event):
    s.send(b'6')
def payment(event):
    s.send(b'7')
def orderi(event):
    s.send(b'8')
def ordertatiuo(event):
    s.send(b'9')
Button1 = tk.Button(text=u'注文',width=5,font=("MSゴシック","20","bold"))
Button1.bind("<Button-1>",orders)
Button1.place(x=130, y=200)
Button2 = tk.Button(text=u'注文',width=5,font=("MSゴシック","20","bold"))
Button2.bind("<Button-1>",orderm)
Button2.place(x=1800, y=200)
Button3 = tk.Button(text=u'注文',width=5,font=("MSゴシック","20","bold"))
Button3.bind("<Button-1>",ordert)
Button3.place(x=130, y=800)
Button4 = tk.Button(text=u'注文',width=5,font=("MSゴシック","20","bold"))
Button4.bind("<Button-1>",ordere)
Button4.place(x=950, y=200)
Button5 = tk.Button(text=u'注文',width=5,font=("MSゴシック","20","bold"))
Button5.bind("<Button-1>",orderk)
Button5.place(x=950, y=800)
Button6 = tk.Button(text=u'注文',width=5,font=("MSゴシック","20","bold"))
Button6.bind("<Button-1>",orderb)
Button6.place(x=1800, y=800)
Button7 = tk.Button(text=u'お会計',width=5,font=("MSゴシック","20","bold"))
Button7.bind("<Button-1>",payment)
Button7.place(x=950,y=400)
Button8 = tk.Button(text=u'注文',width=5,font=("MSゴシック","10","bold"))
Button8.bind("<Button-1>",orderi)
Button8.place(x=650,y=400)
Button9 = tk.Button(text=u'注文',width=5,font=("MSゴシック","10","bold"))
Button9.bind("<Button-1>",ordertatiuo)
Button9.place(x=1800,y=400)
#キャンバスを作り、画像を入れる--------------------------
canvas=tk.Canvas(win,bg="white",width=190,height=150,highlightthickness=0)
canvas.place(x=20,y=30)
canvas.create_image(90,60, image=img2)
canvas=tk.Canvas(win,bg="white",width=190,height=170,highlightthickness=0)
canvas.place(x=1650,y=30)
canvas.create_image(90,80, image=img4)
canvas=tk.Canvas(win,bg="white",width=190,height=170,highlightthickness=0)
canvas.place(x=20,y=600)
canvas.create_image(90,70, image=img6)
canvas=tk.Canvas(win,bg="white",width=190,height=170,highlightthickness=0)
canvas.place(x=850,y=30)
canvas.create_image(90,80, image=img8)
canvas=tk.Canvas(win,bg="white",width=190,height=170,highlightthickness=0)
canvas.place(x=850,y=600)
canvas.create_image(90,80, image=img10)
canvas=tk.Canvas(win,bg="white",width=190,height=170,highlightthickness=0)
canvas.place(x=1650,y=600)
canvas.create_image(90,80, image=img12)
canvas=tk.Canvas(win,bg="white",width=190,height=170,highlightthickness=0)
canvas.place(x=20,y=400)
canvas.create_image(90,80, image=img14)
canvas=tk.Canvas(win,bg="white",width=190,height=170,highlightthickness=0)
canvas.place(x=1650,y=400)
canvas.create_image(90,80, image=img16)
#----------------------------------------------------

#----------------------------------------------------
win.mainloop()

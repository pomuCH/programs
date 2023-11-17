import tkinter as tk
import requests
from PIL import Image
from PIL import ImageDraw
win= tk.Tk()
win.geometry('740x300')
win.configure(bg='white')
win.title('Koizumi.exe')
#画像処理
url = 'https://www.townnews.co.jp/0501/images/a001054475_09.jpg'
r = requests.get(url)
if r.status_code == 200:
    with open('小泉進次郎.jpg', 'wb') as f:
        f.write(r.content)
#jpgからpng--------------------------------------
im = Image.open("小泉進次郎.jpg")
im.save('小泉進次郎.png')
im.save('koizumi.png')
#円形に切り抜く-----------------------------------
path = "小泉進次郎.png"
offset = 80     
img = Image.open(path)
mask = Image.new("L", img.size)
draw = ImageDraw.Draw(mask)
draw.ellipse([(offset, offset), (img.size[0] - offset, img.size[1] - offset)], 255)
del draw
img.putalpha(mask)
img.save("小泉進次郎.png")
#画像の大きさ変更-----------------------------------
from PIL import Image
img1= Image.open('小泉進次郎.png')
img_resize = img1.resize((67,65))
img_resize.save('小泉進次郎.png')
img3=Image.open('koizumi.png')
img_resize=img3.resize((1200,800))
img_resize.save('koizumi.png')
#--------------------------------------------------
img2=tk.PhotoImage(file="小泉進次郎.png",width=65,height=65)
img3=tk.PhotoImage(file="koizumi.png",width=1500,height=650)
lbl = tk.Label(text='error is error',font=("MSゴシック","20","bold"))
lbl.configure(bg='white')
lbl.place(x=300, y=70)
def DeleteEntryValue(event):
    canvas=tk.Canvas(win,width=800,height=300,highlightthickness=0)
    canvas.place(x=0,y=0)
    canvas.create_image(300,250, image=img3)
Button1 = tk.Button(text=u'OK',width=5,font=("MSゴシック","30","bold"))
Button1.bind("<Button-1>",DeleteEntryValue)
Button1.place(x=130, y=200)
Button2 = tk.Button(text=u'OK',width=5,font=("MSゴシック","30","bold"))
Button2.bind("<Button-1>",DeleteEntryValue)
Button2.place(x=300, y=200)
Button3 = tk.Button(text=u'OK',width=5,font=("MSゴシック","30","bold"))
Button3.bind("<Button-1>",DeleteEntryValue)
Button3.place(x=470, y=200)
#キャンバスを作り、画像を入れる--------------------------
canvas=tk.Canvas(win,bg="white",width=60,height=60,highlightthickness=0)
canvas.place(x=235,y=55)
canvas.create_image(30,30, image=img2)
#----------------------------------------------------
win.mainloop()

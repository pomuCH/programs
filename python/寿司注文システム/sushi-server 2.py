import socket
import requests
ip = socket.gethostbyname(socket.gethostname())
port1=8765
socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
socket1.bind((ip, port1))
socket1.listen(5)

url_line = "https://notify-api.line.me/api/notify"
token = "ここには取得したAPIキーを入力してください"
headers = {"Authorization" : "Bearer "+ token}
message =  ip
payload = {"message" :  message}
r = requests.post(url_line, headers = headers, params=payload)

print(f'クライアントからの入力待ち状態 : ip ={ip}')

# コネクションとアドレスを取得
connection, address = socket1.accept()
print('接続したクライアント情報:'  + str(address))

# 無限ループ　byeの入力でループを抜ける
recvline = ''
sendline = ''
num = 0

cnt=0
while True:

    # クライアントからデータを受信
    recvline = connection.recv(4096).decode()

    if recvline == 'bye':
        break
    num=int(recvline)
    if num==1:
        print('サーモンを注文')
        cnt +=10
        url_line = "https://notify-api.line.me/api/notify"
        token = "ここには取得したAPIキーを入力してください"
        headers = {"Authorization" : "Bearer "+ token}
        message =  'サーモン'
        payload = {"message" :  message}
        r = requests.post(url_line, headers = headers, params=payload)
    if num==2:
        print('マグロを注文')
        cnt +=10
        url_line = "https://notify-api.line.me/api/notify"
        token = "ここには取得したAPIキーを入力してください"
        headers = {"Authorization" : "Bearer "+ token}
        message =  'マグロ'
        payload = {"message" :  message}
        r = requests.post(url_line, headers = headers, params=payload)
    if num==3:
        print('タコを注文')
        cnt +=10
        url_line = "https://notify-api.line.me/api/notify"
        token = "ここには取得したAPIキーを入力してください"
        headers = {"Authorization" : "Bearer "+ token}
        message =  'タコ'
        payload = {"message" :  message}
        r = requests.post(url_line, headers = headers, params=payload)
    if num==4:
        print('エビを注文')
        cnt +=10
        url_line = "https://notify-api.line.me/api/notify"
        token = "ここには取得したAPIキーを入力してください"
        headers = {"Authorization" : "Bearer "+ token}
        message =  'エビ'
        payload = {"message" :  message}
        r = requests.post(url_line, headers = headers, params=payload)
    if num==5:
        print('カンパチを注文')
        cnt +=10
        url_line = "https://notify-api.line.me/api/notify"
        token = "ここには取得したAPIキーを入力してください"
        headers = {"Authorization" : "Bearer "+ token}
        message =  'カンパチ'
        payload = {"message" :  message}
        r = requests.post(url_line, headers = headers, params=payload)
    if num==6:
        print('タイを注文')
        cnt +=10
        url_line = "https://notify-api.line.me/api/notify"
        token = "ここには取得したAPIキーを入力してください"
        headers = {"Authorization" : "Bearer "+ token}
        message =  'タイ'
        payload = {"message" :  message}
        r = requests.post(url_line, headers = headers, params=payload)
    if num==7:
        print(f'お会計{cnt*10}円')
        url_line = "https://notify-api.line.me/api/notify"
        token = "ここには取得したAPIキーを入力してください"
        headers = {"Authorization" : "Bearer "+ token}
        message =  f'お会計{cnt*10}円'
        payload = {"message" :  message}
        r = requests.post(url_line, headers = headers, params=payload)
        break
# クローズ
connection.close()
socket1.close()
print('サーバー側終了です')

import socket
import re

url = input('Enter an url: ')
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = re.search('http[s]?://(.*).*', url)
mysock.connect(('data.pr4e.org', 80))
cmd = f'GET {url} HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    try:
        data = mysock.recv(512)
    except:
        print('Please enter a valid url.')
        break
    if len(data) < 1:
        break
    print(data.decode(), end='')

mysock.close()

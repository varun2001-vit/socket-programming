import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=1255
s.bind((host,port))
s.listen(3)
socketclient,add=s.accept()
print("establish connection -",add)
con=True
while con:
    msg=socketclient.recv(1024)
    msg=msg.decode("utf-8")
    print(msg)
    if(msg == "quit"):
        con=False 
s.close( )
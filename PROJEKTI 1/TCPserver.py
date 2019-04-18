from datetime import datetime
from socket import *
import random
import math
from _thread import * 

serverName = 'localhost'
serverPort = 1200
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverName, serverPort))

serverSocket.listen(5)
print("Serveri eshte duke ndegjuar")


def EMRIIKOMPJUTERIT():
    emri=gethostname()
    if not emri:
        mesazhi = "Emri i hostit nuk mund te gjendet"
        return mesazhi
    else:
        return emri

def GRUPIILIGJERATAVE(emri):
    a="abcdefg"
    b="hijklmnopqrstvxyz"
    for shkronja in emri:
        if(shkronja.lower() in a):
           g1="Grupi i pare i ligjeratave" 
           return g1
        elif(shkronja.lower() in b):
           g2="Grupi i dyte i ligjeratave"
           return g2

def IPADRESA(addr):
	return addr[0]

def NUMRIIPORTIT(addr):
	return addr[1]

def BASHKETINGLLORE(fjalia):
    k = 0;
    bashketingelloret = "bcdfghjklmnpqrstvxyz"
    for shkronja in fjalia:
        if(shkronja.lower() in bashketingelloret):
            k += 1
    return k

def KOHA():
    koha = datetime.now();
    #strftime ("%Y.%m.%d %H:%M:%S", koha);
    koha = koha.strftime("%Y.%m.%d %H:%M:%S %p");
    return koha

def LOJA():
    res = ""
    for i in range(7):
        x = random.randint(1,29)
        res += str(x)+","
    return res[:-1]

def FIBONACCI(n):
    first = 0
    second = 1
    for i in range(int(n)-1):
        temp = first
        first = second
        second +=  temp
    return second

def KONVERTIMI(t, i):
    if( t == "KilowattToHorsepower"):
        return i*1.341
    elif( t == "HorsepowerToKilowatt"):
        return i/1.341
    elif( t == "DegreesToRadians"):
        return (i*math.pi)/180
    elif(t == "RadiansToDegrees"):
        return (i*180)/math.pi
    elif(t == "GallonsToLiters"):
        return i*3.78541
    elif(t == "LitersToGallons"):
        return i/3.78541
  


def PRINTIMI(fjalia):
    fjalia = fjalia.lstrip().rstrip();
    return fjalia

def SYPRINA(a,b):
    syprina=a*b
    return syprina

def GRUPIILIGJERATAVE(emri):
    a="abcdefg"
    b="hijklmnopqrstvxyz"
    for shkronja in emri:
        if(shkronja.lower() in a):
           g1="Grupi i pare i ligjeratave" 
           return g1
        elif(shkronja.lower() in b):
           g2="Grupi i dyte i ligjeratave"
           return g2

def Gabimi():
    gabim = "Gabim, keni shtypur vlera jo valide"
    return gabim
    

def start(inputi,addr):
    inputi2 = inputi.split(" ")
    konvertimet = ['KilowattToHorsepower','HorsepowerToKilowatt','DegreesToRadians','RadiansToDegrees','GallonsToLiters','LitersToGallons']
  
    if(inputi[0:15].upper() == "BASHKETINGLLORE" and len(inputi[16:])!=0 ):
        return BASHKETINGLLORE(inputi[16:])
    elif(inputi[0:4].upper() == "KOHA"):
        return KOHA()
    elif(inputi[0:8].upper() == "PRINTIMI" and len(inputi[9:])!=0 ):
        return PRINTIMI(inputi[9:])
    elif(inputi[0:4].upper() == "LOJA"):
        return LOJA()
    elif(inputi[0:9].upper() == "FIBONACCI" and inputi[10:].isdigit() and inputi[10:]!=0):
        return FIBONACCI(inputi[10:])
    elif(inputi[0:16].upper() == "EMRIIKOMPJUTERIT"):
        return EMRIIKOMPJUTERIT()
    elif(inputi[0:12].upper() == "NUMRIIPORTIT"):
        return NUMRIIPORTIT(addr)
    elif(inputi[0:8].upper() == "IPADRESA"):
        return IPADRESA(addr) 
    elif(len(inputi2) > 2 and inputi2[0].upper() == "KONVERTIMI" and (inputi2[1] in konvertimet) and inputi2[2].isdigit()):
        return KONVERTIMI(inputi2[1],int(inputi2[2]))
    elif(inputi[0:4].upper() == "EXIT"):
        return EXIT()
    elif(len(inputi2) > 2 and inputi2[0].upper() == "SYPRINA" and inputi2[1].isdigit() and inputi2[2].isdigit()):
        return SYPRINA(int(inputi2[1]),int(inputi2[2]))
    elif(inputi[0:17].upper() == "GRUPIILIGJERATAVE" and len(inputi[18:])!=0):
        return GRUPIILIGJERATAVE(inputi[18])
    else:
        return Gabimi()
    

def listenToClient(client,address):
    while True:
        data = client.recv(1024)
        data = data.decode()
        print(data)
        if(data != "EXIT"):
            res = str(start(data,address))
            print(res)
            client.send(res.encode())
        else:
            break


while True:
        client, address = serverSocket.accept()
        print("Klienti "+ address[0] + " me portin "+ str(address[1]))
        start_new_thread(listenToClient, (client,address) )



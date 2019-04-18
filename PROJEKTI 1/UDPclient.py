from socket import *
import _thread
import datetime
import random
import math
import sys

print("Projekti 1")
print("KLIENTI TCP-FIEK")
print("Studenti: Genc Balaj")

servername='localhost'
port=1200


print("            Zgjedhni njerin nga funksionet duke shkruar emrin e funksionit:")

print()
print("           Shkruani emrin e njerit nga funksionet, dhe variablat perkatese nese nevojiten si me poshte:")
print("       shtypni:   IPADRESA----------------------------------(shfaq ip adresen)       ")
print("       shtypni:   LOJA------------------------------------- (Nje loje e thjeshte)")
print("       shtypni:   KOHA--------------------------------------(shfaq daten dhe kohen)    ")
print("       shtypni:   EMRIIKOMPJUTERIT--------------------------(shfaq emrin e hostit)    ")
print("       shtypni:   NUMRIIPORTIT------------------------------(shfaq numrin e portit)    ")
print("       shtypni:   PRINTIMI hapsire fjala--------------------(largon hapsirat para dhe pas tekstin qe shtypni)")
print("       shtypni:   BASHKETINGLLORE hapsire fjala-------------(tregon numrin e bashtingelloreve ne tekstin qe shtypni )  ")
print("       shtypni:   FIBONACCI hapsire numrin -----------------(llogarit shumen fibonaci")
print("       shtypni:   KONVERTIMI hapsire lloji hapsire vlera----(konverton)")
print("       shtypni:   SYPRINA hapsire gjatsia hapsire gjeresia--(llogarit syprinen e drejtekendeshit)  ")
print("       shtypni:   GRUPIILIGJERATAVE hapsire emrin-----------(tregon grupin e ligjeratave)")
print("       shtypni:   EXIT        ")
print()


    
   
soketa=socket(AF_INET, SOCK_DGRAM)


while 1:
    var=input("Shkurani metoden :")
    if(var != "EXIT"):
		soketa.sendto(str.encode(var),(servername,port))
		pergjigja, addr=soketa.recvfrom(1024)
		print(pergjigja.decode())
    else:
    	soketa.close()
    	ndalja= "Programi ndaloi!"
    	sys.exit(ndalja)

soketa.close()


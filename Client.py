#!/usr/bin/env python3
import socket
import sys

#Reader function
def reader():
    add = ("localhost",1236)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(add)

    while True:
        #Sending the flight code
        inputStr = input("Please enter a flight code: ")

        action = "READ"
        sendStr = " ".join([action,inputStr])
        print(sendStr)
        sock.sendall(sendStr.encode())

        #Receiving the answer from the server
        data = sock.recv(1024)
        data = data.decode().split(" ")
        #print(data)
        if data[0] == "ROK":
            data.remove("ROK")
            info = " ".join(data)
            print(info)
        else:
            print("Flight wasn't found")

def main():
    if sys.argv[1] == "1":
        reader()
    elif sys.argv[1] == "0":
        writer()

if __name__ == '__main__':
    main()

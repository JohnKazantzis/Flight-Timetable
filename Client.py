#!/usr/bin/env python3
import socket
import sys

def reader():
    add = ("localhost",1235)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(add)

    while True:
        inputStr = input("Please enter a flight code: ")

        action = "READ "
        sendStr = "".join([action,inputStr])
        print(sendStr)
        sock.sendall(sendStr.encode())

        data = sock.recv(1024)
        print(data.decode())

def main():
    if sys.argv[1] == "1":
        reader()
    elif sys.argv[1] == "0":
        writer()

if __name__ == '__main__':
    main()

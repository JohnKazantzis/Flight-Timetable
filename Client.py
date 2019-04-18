#!/usr/bin/env python3
import socket
import sys

#Reader function
def reader(sock):

    while True:
        #Sending the flight code
        inputStr = input("Please enter a flight code: ")

        action = "READ"
        sendStr = " ".join([action,inputStr])
        sock.sendall(sendStr.encode())

        #Receiving the reply from the server
        data = sock.recv(1024)
        data = data.decode().split(" ")
        if data[0] == "ROK":
            data.remove("ROK")
            info = " ".join(data)
            print(info)
        else:
            print("Flight wasn't found")

def writer(sock):

    while True:
        #Sending the desired action and the details of the flight
        action = input("Please enter the action you want to perform (WRITE/DEL/CHANGE): ")
        code = input("Please enter the flight's code: ")
        if action != "DEL":
            state = input("Please enter the flight's state: ")
            dTime = input("Please enter the flight's departure time: ")
            sendStr = " ".join([action,code,state,dTime])
        else:
            sendStr = " ".join([action,code])

        print(sendStr)
        sock.sendall(sendStr.encode())

        #Receiving the reply from the server
        data = sock.recv(1024)
        data = data.decode()
        if data == "WOK":
            print("Flight added")
        elif data == "DOK":
            print("Flight deleted")
        elif data == "CHOK":
            print("Flight changed")
        else:
            print("Error")

def main():
    #Creating the socket and connecting to the server's open port
    add = ("localhost",1236)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(add)

    if sys.argv[1] == "1":
        reader(sock)
    elif sys.argv[1] == "0":
        writer(sock)

if __name__ == '__main__':
    main()

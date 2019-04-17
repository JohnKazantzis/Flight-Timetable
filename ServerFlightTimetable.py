#!/usr/bin/env python
import threading
import socket
import sys

class TimeTable:
    timetable = []

    def addFlight(flight):
        TimeTable.timetable.append(flight)

    def ReturnDetailsStr(index):
        tmpTuple = (TimeTable.timetable[index].code,TimeTable.timetable[index].state,TimeTable.timetable[index].time)
        return " ".join(tmpTuple)

    def SearchFlight(searchItem):
        for x in range(len(TimeTable.timetable)):
            if TimeTable.timetable[x].code == searchItem:
                return x
        return None

class Flight:

    def __init__(self,code,state,time):
        self.code = code
        self.state = state
        self.time = time


def Worker(conn, add):
    while True:
        data = conn.recv(1024)
        protocolData = data.decode().split(" ")
        if protocolData[0] == "READ":
            print(data.decode())
            position = TimeTable.SearchFlight(protocolData[1])
            if position != None:
                conn.sendall(TimeTable.ReturnDetailsStr(0).encode())
            else:
                conn.sendall("Flight wasn't found".encode())


def main():
    f1 = Flight("ah123","boarding","17.30")

    TimeTable.addFlight(f1)
    print(TimeTable.ReturnDetailsStr(0))


    serverAdd = ("localhost",1235)

    #Creating, binding and listening on localhost:1234
    doorSock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    doorSock.bind(serverAdd)
    doorSock.listen(10)

    while True:
        print("Waiting for a connection...")

        conn, add = doorSock.accept()

        t = threading.Thread(target=Worker, args = (conn, add))
        t.start()


if __name__ == '__main__':
    main()

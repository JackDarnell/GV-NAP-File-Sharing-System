#Peer file sharing server, can query server for files and download them
import random
import socket, os, json
from threading import Thread

server_ip = 'localhost'
server_port = 1699
buffer_size = 1000024

#register function, send list of shared files and corresponding keywords to central server


#query function, keyword search


#download function, download file from peer


#upload function, upload file to peer

#---------------------MAIN CODE----------------------------

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_username = ''
#generate a random number between 1 and 3 representing connection speed
#connection_speed = 

def main_thread():
    while True:
        command = input("enter command:")
        if command.split(' ')[0] == 'register':
            hostInfo = input("enter hostname and port with a space in between: ")
            client_socket.connect((hostInfo.split(' ')[0], int(hostInfo.split(' ')[1])))
            # recieveControlThread = Thread(target=recieveControlMessages)
            # recieveControlThread.start()
            client_socket.send(('REGISTER_USER ' + client_username + " " + server_ip + " " + str(random.randint(1,3))).encode())
            message = client_socket.recv(buffer_size).decode()
            print(message)

            # Read JSON file and send file list to server
            with open('files.json', 'r') as f:
                file_list = json.load(f)
            file_list_str = json.dumps(file_list)
            client_socket.send(file_list_str.encode())
            message = client_socket.recv(buffer_size).decode()
            print(message)
        else:
            print('Invalid command')
    print('Exiting main thread')

def recieveControlMessages():
    while True:
        message = client_socket.recv(buffer_size).decode()
        print(message)

client_username = input('Enter username: ')
thread = Thread(target=main_thread)
thread.start()
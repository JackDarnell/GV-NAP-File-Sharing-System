#Peer file sharing server, can query server for files and download them
import random
import socket, os, json
from threading import Thread

server_ip = 'localhost'
server_port = 1699
buffer_size = 1000024


ftp_server_port = 1500
ftp_server_ip = 'localhost'

ftp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ftp_server_socket.bind((server_ip, server_port))
ftp_server_socket.listen()
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
        command = input("enter command: ")
        if command.split(' ')[0] == 'register':
            hostInfo = input("enter hostname server port with a space in between: ")
            client_socket.connect((hostInfo.split(' ')[0], int(hostInfo.split(' ')[1])))
            # recieveControlThread = Thread(target=recieveControlMessages)
            # recieveControlThread.start()
            client_socket.send(('REGISTER_USER ' + client_username + " " + server_ip + " " + str(random.randint(1,3)) + " " + str(ftp_server_port)).encode())
            message = client_socket.recv(buffer_size).decode()
            print(message)

            # Read JSON file and send file list to server
            with open('files.json', 'r') as f:
                file_list = json.load(f)
            file_list_str = json.dumps(file_list)
            client_socket.send(file_list_str.encode())
            message = client_socket.recv(buffer_size).decode()
            print(message)
            #start serving files once registered
            ftp_thread = Thread(target=serve_files)
            ftp_thread.start()
        elif command.split(' ')[0] == 'keyword':
            client_socket.send(('KEYWORD ' + command.split(' ')[1]).encode())
            message = client_socket.recv(buffer_size).decode()
            if message == 'no files found':
                print(message)
            else:
                file_list = json.loads(message)
                for file in file_list:
                    print(file)
        elif command.split(' ')[0] == 'download':
            print('Downloading file')
        else:
            print('Invalid command')
    print('Exiting main thread')

def recieveControlMessages():
    while True:
        message = client_socket.recv(buffer_size).decode()
        print(message)

def serve_files():
    while True:
        ftp_client_socket, ftp_client_address = ftp_server_socket.accept()
        print('Connection from', ftp_client_address)
        while True:
            command = client_socket.recv(buffer_size).decode()
            print('Received', command)
            if command.split(' ')[0] == 'DOWNLOAD':
                fileName = command.split(' ')[1]
                if os.path.isfile(fileName):
                    with open(fileName, 'rb') as f:
                        fileData = f.read()
                    ftp_client_socket.send(fileData)
                else:
                    ftp_client_socket.send('File not found'.encode())


client_username = input('Enter username: ')
thread = Thread(target=main_thread)
thread.start()
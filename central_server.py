#centralized server, indexing all files on the distrubuted system. Other hosts provide info about 
#files they have to the server, and the server provides info about files to other hosts
import socket, os, json
from threading import Thread

server_ip = 'localhost'
server_port = 1600
buffer_size = 1000024

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen()
                        
exampleFile = {'name' : 'file1.txt', 'username' : "TEST", "description" :"test description"}
exampleUser = {'username': ['speed', 'port number', 'host name']}

users = {} #dictionary of users
files = [] #hosts register function USERNAME, HOSTNAME, CONNECTION SPEED


#recieve keyword search from host, return list of files that match keyword

#REGISTER, USERNAME, HOSTNAME, CONNECTION SPEED
def control_thread(client_socket, client_address):
    print('Connection from', client_address)
    currentUser = ''
    while True:
        command = client_socket.recv(buffer_size).decode()
        print('Received', command)
        #if the first word in the command is register, then register the host
        if command.split(' ')[0] == 'REGISTER_USER':
            #add the host to the dictionary of registered hosts
            currentUser = command.split(' ')[1]
            users[command.split(' ')[1]] = {'username': command.split(' ')[1], 'hostname': command.split(' ')[2], 'speed': command.split(' ')[3], 'port': command.split(' ')[4]}
            #send the host a confirmation message
            client_socket.send('register success'.encode())
            file_data = client_socket.recv(buffer_size)
            file_list_json = file_data.decode()
            file_list_new = json.loads(file_list_json)
            for file in file_list_new:
                file['username'] = currentUser
                files.append(file)
            client_socket.send('file list received'.encode())
            for file in files:
                print(file)
        elif command.split(' ')[0] == 'KEYWORD':
            #search the dictionary of files for the keyword
            foundFiles = []
            for file in files:
                if command.split(' ')[1] in file['description']:
                    foundFile = {}
                    foundFile['hostname'] = users[file['username']]['hostname']
                    foundFile['port'] = users[file['username']]['port']
                    foundFile['speed'] = users[file['username']]['speed']
                    foundFile['file_name'] = file['name']
                    foundFiles.append(foundFile)
            #send the host a list of files that match the keyword
            if(len(foundFiles) == 0):
                client_socket.send('no files found'.encode())
            else:
                client_socket.send(json.dumps(foundFiles).encode())
            print(command.split(' ')[1])
        elif command.split(' ')[0] == 'QUIT':
            client_socket.close()
            #remove files from user
            for file in files:
                if file['username'] == currentUser:
                    files.remove(file)
            #remove user from users
            users.pop(currentUser)            
            break
            

while True:
    client_socket, client_address = server_socket.accept()
    thread = Thread(target=control_thread, args=(client_socket, client_address))
    thread.start()
        
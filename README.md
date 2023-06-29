# GV-NAP-File-Sharing-System
A Napster clone for file sharing. A central server stores different users connected and the files they make available to share. Peers can search for files available and then download them by connecting to the peer that hosts the file. Both peers and host are multithreaded. 

## Peer File Sharing
Files shared by the peer should be in the working directory of peer.py. A json file needs to be created to list each file that should be shared, the format is a list of dictionaries, each dict should include the name and description. The description should include the potential keywords that users can search for to find the file. 

## Commands
### Peer:
- `register HOSTNAME PORT_NUMBER`  Registers new peer on the network, prompts user to enter the central server hostname and port to connect.
- `keyword EXAMPLE_WORD`  Performs a search on the central server for files associated with the keyword, returns files found with file host's hostname and port.
- `Download PEER_HOSTNAME PEER_PORT FILENAME` downloads the file into the working directory of the peer.
- `quit`  Closes the connection with the central server and stops serving files.

### Central Server:
- Prompts user for port, no other commands necessary. 

### To-Dos:
- Add automatic files.json creation from within peer. Should prompt user for each file in the current directory.
- Quit command for central server. 
- When central server quits send quit command to peers.
- Error handling for peer commands. 
- Change buffer handling so data larger than the buffer is sent using a loop, recieving code will need to check for a termination character to determine if all of the past message has been sent. 

### Bugs:
- When a client crashes the central server control thread for that client hits an infinite loop, need to find a way to detect when the client disconnects without quitting, clear their files and username, and close the control thread for the client. 
- When client quits the program doesn't exit properly, it appears to exit the main thread and then hang. 
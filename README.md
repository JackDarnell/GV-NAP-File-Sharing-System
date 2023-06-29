# GV-NAP-File-Sharing-System
A Napster clone for file sharing. A central server stores different users connected and the files they make available to share. Peers can search for files available and then download them by connecting to the peer that hosts the file. 

## Commands
### Peer:
- `register HOSTNAME PORT_NUMBER`  Registers new peer on the network, prompts user to enter the central server hostname and port to connect.
- `keyword EXAMPLE_WORD`  Performs a search on the central server for files associated with the keyword, returns files found with file host's hostname and port.
- `Download PEER_HOSTNAME PEER_PORT FILENAME` downloads the file into the working directory of the peer.
- `quit`  Closes the connection with the central server and stops serving files.

# Central Server:
The central server stores the different users as a dictionary and the files as a list of dictionaries too keep track of who is online and what files are available. Clients


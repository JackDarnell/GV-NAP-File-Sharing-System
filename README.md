# GV-NAP-File-Sharing-System
A Napster clone for file sharing. A central server stores different users connected and the files they make available to share. Peers can search for files available and then download them by connecting to the peer that hosts the file. 

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


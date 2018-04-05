# Socket level samples
# Show the three models?
# * dispatching a thread to handle clientsocket
# * create a new process to handle clientsocket
# * restructure this app to use non-blocking sockets
# Probably just the first two


import socket

PORT = 8090
MAX_OPEN_REQUESTS = 5

def process_client(clientsocket):
    print(clientsocket)
    clientsocket.close()


# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to a public host, and a well-known port
hostname = socket.gethostname()
try:
    serversocket.bind((hostname, PORT))
    # become a server socket
    # MAX_OPEN_REQUESTS connect requests before refusing outside connections
    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:
        # accept connections from outside
        print ("Waiting for connections at %s %i" % (hostname, PORT))
        (clientsocket, address) = serversocket.accept() #es un loop infinito, cuando el server se conecta al client para.
        # now do something with the clientsocket
        # in this case, we'll pretend this is a non threaded server
        process_client(clientsocket) #cuando un server y un client se comunican, el primero que tiene que dar el paso es el client, razon por la que existe el loop anterior.

except socket.error:
    print("Problemas using port %i. Do you have permission?" % PORT)

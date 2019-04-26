#!/usr/bin/env python3

import hashlib
import string

def crack():

    # Open and read hashes.txt
    with open("hashes.txt", "r") as h:
        hashes = h.read().splitlines()

    # Open and read passwords.txt
    with open("passwords.txt", "r") as p:
        passwords = p.read().splitlines()
    
    characters = string.ascii_lowercase

    for c in characters:
        for p in passwords:
            
            # crack hashes
            new_password = c + p
            new_hash = hashlib.sha256(new_password).hexdigest()

            # print hashes as 'input:hash'
            # i.e.  yeet:909104cdb5b06af2606ed4a197b07d09d5ef9a4aad97780c2fe48053bce2be52
            if new_hash in hashes:
                print new_password,":",new_hash

if __name__ == "__main__":
    crack()

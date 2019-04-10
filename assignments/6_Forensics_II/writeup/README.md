# Writeup 6 - Forensics

Name: *PUT YOUR NAME HERE
Section: *PUT YOUR SECTION NUMBER HERE*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: *PUT YOUR NAME HERE*

## Assignment Writeup

### Part 1 (45 Pts)

1. The IP address being attacked is 142.93.136.81 I used Wireshark to analyze netlog.pcap and I found this IP to be the server because
data was first sent to it. This IP also is the one that requests the username and password.

2. Based on the packet capture, I can infer that tools were used to scan for open ports on the victim's machine. Nmap is a tool that could have been used to do this.

3. The hackers' IP addresses are 159.203.113.181 and this IP is from New Jersey.

4. They are using port 20 to steal files on the server. In the FTP-DATA files, the source is 20.

5a. They stole a jpeg file through the FTP-DATA protocol. To view the jpeg, I follwed the packet (2080) that had the FTP-DATA protocol which meant data was being transfered. I then exported the packet payload as raw onto this assignmnet folder. I was able to then open the picture and see it.

5b. This photo was taken in Parada 1 at Barava Beach in Pundta del Este, a popular resort town in Uruguay. The sculpture in the picture is La Mano.

5c. This picture was taken on December 23, 2018 and the timestamp is 2018:12:23 17:16:24. I got this information by looking at the proprerties of the photo.

5d. An Apple iPhone 8 back camera took this photo. The flash did not fire.

5e. The GPSaltitude of this photo was 4.5726 meters.

6. The attackers left a file called greetz.fpff on the server.

7. One way to defend against port scan attacks is to use the same tools to hack yourself. By using Nmap on your own device, you can see what ports are open or closed. From then, you can check to see if you really need these ports to be open. Implementing a firewall can help
defend against these tools because they can close ports and reroute the traffic.

### Part 2 (55 Pts)

i. greetz.fpff was generated on 2019-03-27, 04:15:05

ii. fl1nch wrote this file.

iii.

iv. The first flag I found was CMSC389R-{h0pefully_y0u_didnt_grep_CMSC389R}. I found this flag during looking at the data from following the TCP stream. However it was backwards ( }R983CSMC_perg_tndid_u0y_yllufep0h{- ) so I had to reverse it.

# Writeup 3 - Operational Security and Social Engineering

Name: Tuan Le
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: Tuan Le

## Assignment Writeup

### Part 1 (40 pts)

To collect all of this information, my plan would use multiple apporaches as I feel it woujld be very difficult to obtain everything with one method. To find Moffet's mother's maiden name, I would create a spear phishing email to Moffet. I would make this email seem like it is coming from the head of her human resources at 1337Bank by spoofing it. The email would be personable, properly greeting Moffet with her name and ending with a proper friendly goodbye.The purpose of the email is to ask her to update her account information and emergency contacts. There would be a link in the email where Moffet would then go to enter the information. I would craft this email to be as genuine as possbile by using the same font, format, company logos, etc. Since it is coming from someone she knows, she is likely to follow the link. In this link, I would also ask her to input her Internet browser of choice. The rationale behind this would be for the company to obtain a better guage of what web services their employees want to use.

I would do something similar for her city of birth and first pet name. I would fake an email from Twitter to Moffet, because I know she has a Twitter account, and in the email I would say that Twitter is updating their terms of service and privacy settings. By this, all users need to create new password questions to improve their security. The questions asked would be "what city were you born in?" and "what was the name of your first pet?" I may throw in an extra question of choice so it appears less rigid and forced. Of course, I would spoof the email so it looks like its coming from the IT division at Twitter. This is a sensible elicitation because Moffet will think it is harmless. Emails like this are pretty common among social media sites and thus she may not give it a second thought.

However, for the ATM pin number, I would call her bank company. Similar to the video we watched in class, I would pretend to be her husband and have baby crying noises in the background. As her fake husband, I would try to get the company to reveal the pin number to me. I would try to appear upset and exhausted in the phone call in order to help gain the sympathy of whoever I was talking to. If the employee asks me questions that I do not know, I would try to deflect and maybe give an answer that is correct about Moffet, but may not answer the concern completely. I would just stress that I am tired and need to get the pin so I can take care of the baby and prepare dinner. Lying about social security numbers is also valid, as seen in the video.

### Part 2 (60 pts)

The first and easiest vulnerability for Moffet to fix is her password. It is very simple and thus can easily be brute forced. Her password "linkinpark" is very weak because it does not include captial and lowercase letters, numbers, and special characters. The only good thing about her password is that it is at least 8 characters long. These are characterisitcs of strong passwords as stated by Lafayette College in their article "Guidelines for Strong Passwords." She could possibly change her password to L1nk1nP@rk69! This complex combination of characters and increased length will make it incredibly difficult for any brute force script to crack. Furthermore, the this new password will not be common because there are no longer dictionary words dude to numbers replacing the characters. On another note, she should not sure the same password for multiple accounts just in case one of the accounts is breached.

The second vulnerability is her open ports. She had three ports open which opens her to inflitrations from the outside. Unguarded open ports can be used to spread malware among other attacks. Although open ports are not necessarily a bad thing, there is nothing to guard those open ports. According to Acunetix's article "Danger: Open Ports - Trojan is as Trojan does" the best practice is to use a firewall system that controls which ports are opened or closed. A firewall would ensure that ports should only be open if they need to be, instead of just always open. By implementing a firewall, Moffet will prevent her ports from exposing her to hackers and thus protect her applications and services behind those ports. The firewall can also be configured to allow traffic on the ports they use and this traffic can be monitored. 

The third vulnerability is in the website's source code. I was able to find the username and password by just examining the source code of the website. As a result, I was able to login in using the creditals. This is bad for obvious reasons. An attacker can copy, tamper, and delete files once they have access. To fix this, Moffet must not store passwords in the website's source code. According to CERN Computer Security's recommendations, keeing the passowords in a separate file will make them easier to guard. Such a file should have very restrictive file permissions. Also, encrypting the password is a great idea and there are many libraries that provide encryption algorithms like RSA. Furthermore, once encrypted, the data should also be stored a separate file like mentioned before. In general, it is a terrible idea to store login information within source code as it is in plain sight.




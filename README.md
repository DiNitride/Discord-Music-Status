# Discord-Music-Status
## A Program to display your currently played Music as your Discord Status

The status won't display on your own client for some reason, Discord's fault, however if you look on another client or mobile you see it will be displayed.

![Sidebar](http://storage.dinitride.win/sidebar_example.png)

![Profile](http://storage.dinitride.win/profile_example.png)

##### The program will work with:
- Spotify
- iTunes
- Winamp
- foobar2000
- VLC
- Google Play Music Desktop Player
- Quod Libet

##### Requirements:
- Python 3.6
- Discord.py and Logbook installed via pip
- Snip / https://github.com/dlrudie/Snip/releases/latest

##### Install:
1. Install requirements above
2. Start up snip, this must be done at least once before starting the script, and snip **must be running while you use it!**
3. Find your Discord token *See below*
4. Run `run.py` to generate a config file
5. Configure the file with your token and path to snip.txt *Neither should have quotation marks*
6. Start `run.py`

*Example Config*
```
[Config]
token = mfa.a4g2Wazb... 
snip = D:\DiNitride\Snip\Snip.txt
```

*Your token will only be prefixed with mfa if you have 2 factor auth enabled*

##### Finding Login Token
1. Open Discord
2. Press Ctrl+Shift+i
3. Click "Application" tab
4. Expand Storage > Local Storage > https://discordapp.com/
5. Find "token" under "key"
6. Copy the text in quotes on the same row, DO NOT KEEP THE QUOTES

##### Logging out
To log out, send "m.quit" anywhere on Discord

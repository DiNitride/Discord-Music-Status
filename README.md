# Discord-Music-Status
## A Program to display your currently played Music as your Discord Status

The status won't display on your own client for some reason, Discord's fault, however if you look on another client or mobile you see it will be displayed.

![Sidebar](http://storage.dinitride.win/sidebar_example.png)

![Profile](http://storage.dinitride.win/profile_example.png)

#### The program will work with:
- Spotify
- iTunes
- Winamp
- foobar2000
- VLC
- Google Play Music Desktop Player
- Quod Libet

#### Requirements:
- Python 3.6
- Discord.py and Logbook installed via pip
- Snip / https://github.com/dlrudie/Snip/releases/latest

### Install:
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

#### Finding Login Token
1. Open Discord
2. Press Ctrl+Shift+i
3. Click "Application" tab
4. Expand Storage > Local Storage > https://discordapp.com/
5. Find "token" under "key"
6. Copy the text in quotes on the same row, DO NOT KEEP THE QUOTES

#### Installing Logbook and Discord via Pip

Open command prompt, and type `pip install logbook` and `pip install discord.py`
This should install both modules

If for some reason it doesn't, [read here](https://packaging.python.org/tutorials/installing-packages/)

### FAQ and Troubleshooting
This program has been tested and is 100% functional, providing the enviroments it is run in are correct.

###### Ensure Discord.py is updated to the latest version
A breaking change may have happened to the Discord API, which is out of my control, and you will need to update your installation. In the event that the problem is not fixed by the library, and I need to update my code, please open an issue in the issues tab.

###### Make sure your config is set up correctly
Study the example config above and make sure that your paths **are pointing to the correct file**
*snip.exe IS NOT the correct file, snip.txt is, this will cause an error*

**Do not add me as a friend on Discord and DM me for help.**
Github has an issues feature which works perfectly well, allows me to keep track of problems better, and in turn allows others to see the solution when we get to it.

#### Logging out
To log out, send "m.quit" anywhere on Discord and the script should log you out properly


### Lots of love, DiNitride xoxoxo

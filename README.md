# Discord-Music-Status
## A Program to display your currently played Music as your Discord Status
This project is legacy. Discord has implemented this as a native feature for Spotify. As suchg, this project is no longer maintained.

**WARNING: Using a self-bot is technically against Discord's TOS (I originally wrote this when Discord had no statement on them and they were allowed), I am not accountable for any action they take due to you running this bot.**

#### The program will work with:
- Spotify
- iTunes
- Winamp
- foobar2000
- VLC
- Google Play Music Desktop Player
- Quod Libet

#### Requirements:
- Python 3.6+
- Discord.py and Logbook python modules installed via pip
  `pip install logbook`
  `pip install discord.py`
- Snip / https://github.com/dlrudie/Snip/releases/latest. *Due to Snip being Windows only, the default install instructions will only be applicable for Windows. However as the script is Python, as long as you find some program to spit out your music to a text file, you can configre that text file instead and it will run on any machine Python will run on*

### Install:
1. Install requirements above
2. Start up snip, this must be done at least once before starting the script, and snip **must be running while you use it!**
3. Find your Discord token *See below*
4. Run `run.py` to generate a `config.ini` file (If a file is not generated, see FAQ)
5. Configure the file with your token and path to snip.txt *Neither should have quotation marks*
6. Start `run.py`. The status will not show up for you, as Discord does not display it on your own client when you edit it. I cannot fix this. Your friends will be able to see it however, or you can log into another account and check.

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

### FAQ and Troubleshooting
###### Ensure Discord.py is updated to the latest version
A breaking change may have happened to the Discord API, which is out of my control, and you will need to update your installation. In the event that the problem is not fixed by the library, and I need to update my code, please open an issue in the issues tab.

`pip install discord.py --upgrade`
or
`python -m pip install discord.py --upgrade`

###### Config file is not genereated!
If after running the `run.py` once you find no config file has been generated, then please try running the script within a command prompt or terminal window with Python directly (`C:\Users\DiNitride\Path\To\Dir>python run.py` or `$ python run.py`) so you can see the output. There may be another unresolved issue which you cannot otherwise see. Another issue is that the script may not have permissions to create a file, try running as administrator. If you still cannot create a config file, try creating one manually.

###### Make sure your config is set up correctly
Study the example config above and make sure that your paths **are pointing to the correct file**
*snip.exe IS NOT the correct file, snip.txt is, this will cause an error*

**Do not add me as a friend on Discord and DM me for help.**
Github has an issues feature which works perfectly well, allows me to keep track of problems better, and in turn allows others to see the solution when we get to it.

#### Logging out
To log out, send "m.quit" anywhere on Discord and the script should log you out properly

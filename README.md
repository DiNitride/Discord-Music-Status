# Discord-Music-Status
## A Program to display your currently played Music as your Discord Status

The status won't display on your own client for some reason, Discord's fault, however if you look on another client or mobile you see it will be displayed.

###### The program will work with:
- iTunes
- Spotify
- VLC
- Winamp
- Foobar2000
- (Any other program Snip is updated to be able to access)

###### Requirements:
- Discord.py / https://github.com/Rapptz/discord.py
- Snip / https://github.com/dlrudie/Snip/releases/latest

###### Install:
1. Install Snip and run at least once, to generate snip.txt
2. Find your Discord Login token (See "Finding Login Token below")
3. Update defaultconfig.ini with your token and path to snip.txt, your path to snip.txt should look something like this. `C:\Users\User\Documents\Snip\snip.txt`
4. Rename defaultconfig.ini to config.ini **IMPORTANT**
5. Run `run.py`

###### Finding Login Token
1. While on the Discord Desktop app press `ctrl + shift + i`
2. Switch to `console` tab
3. type `localStorage.token` and press enter
4. Copy the token inside the quotation marks

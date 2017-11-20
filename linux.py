import dbus
from dbus.mainloop.glib import DBusGMainLoop
import pympris

dbus_loop = DBusGMainLoop()
bus = dbus.SessionBus(mainloop=dbus_loop)

def pull_song():
    try:
        players_ids = list(pympris.available_players())
        mp = pympris.MediaPlayer(players_ids[0], bus)
        metadata = metadata = mp.player.Metadata
        title = str(metadata['xesam:title'])
        artist = str(metadata['xesam:artist'][0])
        Nowplay = title + " by " + artist
    except (IndexError, KeyError):
        # Rhythm box will make metadata empty when nothing is playing, this also catches no players at all
        Nowplay = ""
    return Nowplay

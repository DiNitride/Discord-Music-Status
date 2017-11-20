snippath=""
def init(snip):
    if snip == "" and sys.platform.startswith('win'):
        logger.critical("No path to snip set! Exiting")
        time.sleep(5)
        exit(1)
    else:
        snippath = snip

def pull_song():
    with open(snippath, encoding="utf-8") as f:
        return f.read()

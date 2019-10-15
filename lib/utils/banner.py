import time

from colorama import Fore, Style

from lib import __version__ as version

class Banner:
    r = Fore.RED
    y = Fore.YELLOW
    ny = Fore.YELLOW
    nw = Fore.WHITE
    g = Fore.GREEN
    e = Style.RESET_ALL

    def banner(self):
        print(self.ny +" __  _ _")                                            
        print(self.ny + "/ _\(_) |_ ___  ___  ___ __ _ _ __  _ __   ___ _ __ ")
        print(self.ny + "\ \ | | __/ _ \/ __|/ __/ _` | '_ \| '_ \ / _ \ '__|")
        print(self.ny + "_\ \| | ||  __/\__ \ (_| (_| | | | | | | |  __/ |   ")
        print(self.ny +"\__/|_|\__\___||___/\___\__,_|_| |_|_| |_|\___|_|   ")
        print(self.y+"      Sitescan - Web Scanner Version 1.0")
        print(self.r+"      Rapid safeGaurd")
        print(self.r+"      www.rapidsafeguard.com")
        print("\n")

    @classmethod
    def preamble(cls, url):
        print('URL: %s' % url)
        print('---------  Scan Started: %s ---------' % (time.strftime('%d/%m/%Y %H:%M:%S')))

    @classmethod
    def postscript(cls):
        print('---------  Scan Finished: %s ---------' % (time.strftime('%d/%m/%Y %H:%M:%S')))

    def version(self):
        return self.g + "~/#" + self.e + " Sitescanner (" + version + ")\n"

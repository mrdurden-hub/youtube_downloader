from modules.Youtube_downloader_mp3 import Youtube_Downloader_mp3
from modules.Youtube_downloader_mp4 import Youtube_Downloader_mp4
from modules.Youtube_downloader_playlist import Youtube_Downloader_playlist


class Main:
    def __init__(self):
        while True:
            q = input('Você quer baixar mp3, video ou uma playlist? ')
            if q == 'mp3':
                Youtube_Downloader_mp3()
                return

            if q and q == 'video':
                Youtube_Downloader_mp4()
                return

            if q and q == 'playlist':
                Youtube_Downloader_playlist()
                return


if __name__ == '__main__':
    Main()

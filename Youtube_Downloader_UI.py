import sys
from UI.design import *
from PyQt5.QtWidgets import QMainWindow, QApplication

from modules.Youtube_downloader_mp3 import Youtube_Downloader_mp3
from modules.Youtube_downloader_mp4 import Youtube_Downloader_mp4
from modules.Youtube_downloader_playlist import Youtube_Downloader_playlist
from modules.Youtube_downloader_playlist_mp4 import Youtube_Downloader_playlist_mp4


class Youtube_downloader(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.setWindowTitle('Youtube Downloader')

        self.download_btn.clicked.connect(self.download)

    def download(self):
        if self.btn_mp3.isChecked():
            self.download_mp3()

        if self.btn_mp4.isChecked():
            self.download_mp4()

        if self.btn_playlist_mp3.isChecked():
            self.download_playlist_mp3()

        if self.btn_playlist_mp4.isChecked():
            self.download_playlist_mp4()

    def download_mp3(self):
        url = self.input.text()
        Youtube_Downloader_mp3(url)

    def download_mp4(self):
        url = self.input.text()
        Youtube_Downloader_mp4(url)

    def download_playlist_mp3(self):
        url = self.input.text()
        Youtube_Downloader_playlist(url)

    def download_playlist_mp4(self):
        url = self.input.text()
        Youtube_Downloader_playlist_mp4(url)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    yd = Youtube_downloader()
    yd.show()
    qt.exec_()

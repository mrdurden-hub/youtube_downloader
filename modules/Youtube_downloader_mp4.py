from pytube import YouTube  # Importando lib necessária para o download
from pytube.cli import on_progress  # importando lib para barra de progresso
import os  # importando a lib necessária para renomear no arquivo
from PyQt5.QtWidgets import QMessageBox


class Youtube_Downloader_mp4:
    # __init__ é o construtor da classe e 'self' referencia a instância da próŕia classe
    def __init__(self, link):
        self.download(link)

    def download(self, link):
        yt = YouTube(link, on_progress_callback=on_progress, )
        stream = yt.streams.get_highest_resolution()
        os.chdir('/home/matt/Vídeos')
        out_file = stream.download()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(f'{out_file} baixado com sucesso.')
        msg.exec_()

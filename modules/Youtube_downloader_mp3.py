from pytube import YouTube  # Importando lib necessária para o download
from pytube.cli import on_progress  # importando lib para barra de progresso
import os  # importando a lib necessária para renomear no arquivo
from PyQt5.QtWidgets import QMessageBox


class Youtube_Downloader_mp3:
    # __init__ é o construtor da classe e 'self' referencia a instância da próŕia classe
    def __init__(self, link):
        self.download(link)

    def download(self, link):
        yt = YouTube(link, on_progress_callback=on_progress, )
        ys = yt.streams.get_audio_only()
        os.chdir('/home/matt/Música')
        out_file = ys.download()
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(f'{out_file} baixado com sucesso.')
        msg.exec_()

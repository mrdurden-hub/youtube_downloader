from pytube import Playlist  # Importando lib necessária para o download
from pytube.cli import on_progress  # importando lib para barra de progresso
import os  # importando a lib necessária para renomear no arquivo
from PyQt5.QtWidgets import QMessageBox


class Youtube_Downloader_playlist:
    # __init__ é o construtor da classe e 'self' referencia a instância da próŕia classe
    def __init__(self, link):
        self.download(link)

    def download(self, link):
        user = os.environ['USERNAME']
        path_folder = f'/home/{user}/Youtube_downloader'

        try:
            os.mkdir(path_folder)
        except FileExistsError as e:
            pass

        os.chdir(path_folder)
        p = Playlist(link)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(f'{p.title} está em Download. Por favor aguarde...')
        msg.exec_()

        for video in p.videos:
            out_file = video.streams.first().download()
            original_name, extension = os.path.splitext(out_file)
            renamed_file = original_name + '.mp3'
            os.rename(out_file, renamed_file)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(f'{p.title} baixado com sucesso.')
        msg.exec_()

from PyQt5 import QtWidgets
import design
import sys
from pytube import YouTube, Playlist
from ffmpeg import output, input, run
from os import remove, path
import threading


def name_reformat(name):
    ban_symbols = ['\\', '/', ':', '*', '?', '"', '<', '>', '|', '.', "'", '$']
    for x in ban_symbols:
        name = name.replace(x, ' ')
    return name


class YouSound(QtWidgets.QWidget, design.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.on_click)

    def logs_add(self, text):
        self.plainTextEdit.appendPlainText(text)
        self.plainTextEdit.update()

    def progressbar_start(self):
        self.progressBar.setMaximum(0)

    def progressbar_stop(self):
        self.progressBar.setMaximum(100)

    def download_video(self):
        try:
            video_example = YouTube(self.url)
            file_name = name_reformat(video_example.title)

            input_name = file_name + '.mp4'
            output_name = file_name + '.mp3'

            if path.exists(input_name) or path.exists(output_name):
                self.logs_add('File already exist')
                self.progressbar_stop()
                return
            else:

                self.logs_add(f'Downloading {video_example.title}...')
                video_example.streams.filter(only_audio=True).first().download(filename=file_name)
                stream = input(input_name)
                audio = stream.audio
                stream = output(audio, output_name, loglevel='quiet')
                run(stream)

                remove(input_name)
                self.progressbar_stop()

        except:
            self.logs_add('Error!')
        self.pushButton.setDisabled(False)

    def download_playlist(self):
        try:
            playlist_example = Playlist(self.url)
            urls = playlist_example.video_urls

            for link in urls:
                video_example = YouTube(link)
                file_name = name_reformat(video_example.title)

                input_name = file_name + '.mp4'
                output_name = file_name + '.mp3'

                if path.exists(input_name) or path.exists(output_name):
                    self.logs_add('File already exist')
                    self.progressbar_stop()
                    self.pushButton.setDisabled(False)
                    return
                else:
                    self.logs_add(f'Downloading {video_example.title}...')

                    video_example.streams.filter(only_audio=True).first().download(filename=file_name)
                    stream = input(input_name)
                    audio = stream.audio
                    stream = output(audio, output_name, loglevel='quiet')
                    run(stream)

                    remove(input_name)

            self.progressbar_stop()
            self.pushButton.setDisabled(False)
            self.logs_add('Playlist was downloaded')

        except:
            self.logs_add('Error!')

    def on_click(self):
        self.pushButton.setDisabled(True)
        self.url = self.lineEdit.text()
        if 'https://www.youtube.com/watch?v=' in self.url or 'https://music.youtube.com/watch?v=' in self.url:
            self.progressbar_start()
            threading.Thread(target=self.download_video, args=()).start()
        elif 'https://www.youtube.com/playlist?list=' in self.url:
            self.progressbar_start()
            threading.Thread(target=self.download_playlist, args=()).start()
        else:
            self.logs_add("Link is incorrect")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = YouSound()
    window.show()
    app.exec_()
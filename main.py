from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock
import threading
from pytubefix import YouTube
import certifi
import os
os.environ['SSL_CERT_FILE'] = certifi.where()

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        self.url = TextInput(multiline=False)
        layout.add_widget(self.url)

        self.progress_bar = ProgressBar(max=100, value=0)
        layout.add_widget(self.progress_bar)

        button = Button(text='Submit')
        button.bind(on_press=self.submit_text)
        layout.add_widget(button)

        self.status_label = Button(text='Ready', disabled=True)
        layout.add_widget(self.status_label)

        return layout

    def submit_text(self, instance):
        self.status_label.text = 'Downloading...'
        self.progress_bar.value = 0
        threading.Thread(target=self.download_video).start()

    def download_video(self):
        url = self.url.text
        try:
            yt = YouTube(url)
            stream = yt.streams.get_highest_resolution()
            yt.register_on_progress_callback(self.update_progress)
            stream.download("/storage/emulated/0/Download/")
            self.status_label.text = 'Download Complete!'
        except Exception as e:
            self.status_label.text = 'Error: ' + str(e)

    def update_progress(self, stream, chunk, bytes_remaining):
        bytes_downloaded = stream.filesize - bytes_remaining
        progress = int((bytes_downloaded / stream.filesize) * 100)
        self.progress_bar.value = progress

if __name__ == '__main__':
    MyApp().run()
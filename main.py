from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.progressbar import ProgressBar
from threading import Thread


class MyBoxLayout(BoxLayout):

    def __init__(self, **kwargs):
        super(MyBoxLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        #self.c = Client(language="en")

        self.url_input = TextInput(hint_text='Enter URL', multiline=False)
        self.add_widget(self.url_input)

        self.submit_button = Button(text='Download Video')
        self.submit_button.bind(on_press=self.download_video)
        self.add_widget(self.submit_button)

        self.progress_bar = ProgressBar(max=100)  # Progress bar with maximum value of 100
        self.add_widget(self.progress_bar)

    def download_video(self, instance):

        download_thread = Thread(target=self.raw_download)
        download_thread.start()

    def raw_download(self):
        url = self.url_input.text
        #video = self.c.get(url)
        #path = "/storage/emulated/0/"
        #quality = Quality.BEST
        #video.download(path=path, quality=quality, callback=self.update_progress)


    def update_progress(self, pos, total):
        percentage_complete = (pos / total) * 100
        self.progress_bar.value = percentage_complete

class MyApp(App):

    def build(self):
        return MyBoxLayout()

if __name__ == '__main__':
    MyApp().run()

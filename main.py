from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.progressbar import ProgressBar
from threading import Thread
try:
    from phub import Client, Quality

except Exception as e:
    exception = True
    exception_text = e

exception = False

class MyBoxLayout(BoxLayout):

    def __init__(self, **kwargs):
        super(MyBoxLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.c = Client(language="en")

        if exception:
            self.url_input = TextInput(hint_text=str(exception_text), multiline=False)
        else:
            self.url_input = TextInput(hint_text="Enter URL:", multiline=False)

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
        video = self.c.get(url)
        path = "/storage/emulated/0/"
        quality = Quality.BEST
        try:
            video.download(path=path, quality=quality, callback=self.update_progress)
        except Exception as e:
            self.url_input.hint_text = str(e)

    def update_progress(self, pos, total):
        percentage_complete = (pos / total) * 100
        self.progress_bar.value = percentage_complete

class MyApp(App):

    def build(self):
        return MyBoxLayout()

if __name__ == '__main__':
    MyApp().run()

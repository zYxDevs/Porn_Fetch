from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.progressbar import ProgressBar
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from threading import Thread
from plyer import filechooser
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

    def show_popup(self, title, message):
        popup = Popup(title=title,
                      content=Label(text=message),
                      size_hint=(None, None), size=(400, 400))
        popup.open()

    def get_download_path(self):
        return filechooser.get_downloads_dir()

    def download_video(self, instance):

        download_thread = Thread(target=self.raw_download)
        download_thread.start()

    def raw_download(self):
        try:
            url = self.url_input.text
            video = self.c.get(url)
            Clock.schedule_once(lambda dt: self.show_popup("Success", "URL erfolgreich geladen!"))

            path = self.get_download_path()
            quality = Quality.BEST
            video.download(path=path, quality=quality, callback=self.update_progress)
            Clock.schedule_once(lambda dt: self.show_popup("Success", "Video erfolgreich heruntergeladen!"))
        except Exception as e:
            Clock.schedule_once(lambda dt: self.show_popup("Error", str(e)))

    def update_progress(self, pos, total):
        percentage_complete = (pos / total) * 100
        self.progress_bar.value = percentage_complete

class MyApp(App):

    def build(self):
        return MyBoxLayout()

if __name__ == '__main__':
    MyApp().run()

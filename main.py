from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.progressbar import ProgressBar
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from threading import Thread

try:
    import phub

    text = "Sucessfully imported PHUB"
    exception = False

except Exception as e:
    exception = True
    text = str(e)


class MyBoxLayout(BoxLayout):

    def __init__(self, **kwargs):
        super(MyBoxLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'

        if exception:
            self.url_input = TextInput(hint_text=str(text), multiline=False)

        else:
            self.url_input = TextInput(hint_text=str(text), multiline=False)

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

    def download_video(self, instance):

        download_thread = Thread(target=self.raw_download)
        download_thread.start()

    def raw_download(self):
        try:
            c = phub.Client()
            url = self.url_input.text
            video = c.get(url)
            Clock.schedule_once(lambda dt: self.show_popup("Success", "URL erfolgreich geladen!"))

            path = "/storage/emulated/0/Download/"
            quality = phub.Quality.BEST
            video.download(path=path, quality=quality, callback=self.update_progress)
            Clock.schedule_once(lambda dt: self.show_popup("Success", "Video erfolgreich heruntergeladen!"))
        except Exception as exc:
            Clock.schedule_once(lambda dt, exc=exc: self.show_popup("Error", str(exc)))

    def update_progress(self, pos, total):
        percentage_complete = (pos / total) * 100
        self.progress_bar.value = percentage_complete


class MyApp(App):

    def build(self):
        return MyBoxLayout()


if __name__ == '__main__':
    MyApp().run()

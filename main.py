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
    import phub
    text = """
Successfully imported PHUB. You can copy / paste the URL in this little input field here and click
on the Download button, and if you are lucky enough, then you see the progressbar doing something ;) 
"""
    exception = False

except Exception as e:
    exception = True
    text = f"There was an error importing phub. Please report the following: {e}"

class MyBoxLayout(BoxLayout):

    def __init__(self, **kwargs):
        super(MyBoxLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.chosen_path = None
        self.path_set = False

        if exception:
            self.url_input = TextInput(hint_text=str(text), multiline=True)

        else:
            self.url_input = TextInput(hint_text=str(text), multiline=True)

        self.add_widget(self.url_input)

        # Add button for specifying download location
        self.path_button = Button(text='Specify Download Location')
        self.path_button.bind(on_press=self.open_filechooser)
        self.add_widget(self.path_button)

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

    def open_filechooser(self, instance):
        try:
            path = filechooser.choose_dir(title="Select Folder")
            if path:
                self.chosen_path = path[0]
                self.path_set = True
        except Exception as e:
            error_msg = f"Error in open_filechooser: {type(e).__name__} - {str(e)}"
            self.show_popup("Error", error_msg)


    def download_video(self, instance):
        if not self.path_set:
            self.show_popup("Error", "Please specify a download location first.")
            return

        download_thread = Thread(target=self.raw_download)
        download_thread.start()

    def raw_download(self):
        try:
            c = phub.Client()
            url = self.url_input.text
            video = c.get(url)
            path = self.chosen_path
            quality = phub.Quality.BEST
            video.download(path=path, quality=quality, callback=self.update_progress)

        except Exception as exc:
            error_details = f"{type(exc).__name__}: {str(exc)}"
            Clock.schedule_once(lambda dt, err=error_details: self.show_popup("Error", err))

    def update_progress(self, pos, total):
        percentage_complete = (pos / total) * 100
        self.progress_bar.value = percentage_complete


class MyApp(App):

    def build(self):
        return MyBoxLayout()


if __name__ == '__main__':
    MyApp().run()

import threading
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.progressbar import MDProgressBar
from kivy.clock import Clock
from plyer import filechooser
from phub import Quality, Client
from kivy.core.clipboard import Clipboard
# Make sure to import other necessary modules and classes like Client, Quality, and filechooser

class DownloadApp(MDApp):
    def build(self):
        layout = MDBoxLayout(orientation='vertical', padding=10, spacing=10)

        # Creating a horizontal layout for the Label and the TextField
        h_layout = MDBoxLayout(spacing=10)
        h_layout.add_widget(MDLabel(text="Enter URL:"))
        self.url_input = MDTextField()
        h_layout.add_widget(self.url_input)

        # Creating a Button
        download_button = MDRaisedButton(text="Download", on_release=self.start_download_thread)
        self.progress_bar = MDProgressBar(value=0, max=100)
        clipboard_button = MDRaisedButton(text="Paste from Clipboard", on_release=self.paste_from_clipboard)

        # Adding widgets to the main layout
        layout.add_widget(h_layout)
        layout.add_widget(download_button)
        layout.add_widget(clipboard_button)
        layout.add_widget(self.progress_bar)

        return layout

    def paste_from_clipboard(self, instance):
        # Get the content from the clipboard and set it as the text of the TextField
        clipboard_content = Clipboard.get()
        self.url_input.text = clipboard_content

    def start_download_thread(self, instance):
        # Start the download in a new thread
        download_thread = threading.Thread(target=self.download)
        download_thread.start()

    def download(self):
        # Get the URL from the TextField
        try:
            url = self.url_input.text
            self.choose_file()
            # You can add the logic to download from the URL here
            cl = Client(language="en")
            video = cl.get(str(url))
            quality = Quality.BEST
            path = self.path[0]
            video.download(path=f"/{path}", quality=quality, display=self.update_progress)
            self.url_input.text = "Started Download"

        except Exception as e:
            self.url_input.text = str(e)


    def update_progress(self, pos, total):
        # Schedule the progress bar update to run in the main thread
        Clock.schedule_once(lambda dt: setattr(self.progress_bar, 'value', (pos / total) * 100))

    def choose_file(self):
        filechooser.choose_dir(on_selection=self.selected)

    def selected(self, selection):
        self.path = selection

# Don't forget to run your app
if __name__ == '__main__':
    DownloadApp().run()
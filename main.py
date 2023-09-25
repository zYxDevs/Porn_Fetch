from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from plyer import filechooser
from kivymd.uix.progressbar import MDProgressBar
from phub import Quality, Client


class DownloadApp(MDApp):
    def build(self):
        layout = MDBoxLayout(orientation='vertical', padding=10, spacing=10)

        # Creating a horizontal layout for the Label and the TextField
        h_layout = MDBoxLayout(spacing=10)
        h_layout.add_widget(MDLabel(text="Enter URL:"))
        self.url_input = MDTextField()
        h_layout.add_widget(self.url_input)

        # Creating a Button
        download_button = MDRaisedButton(text="Download", on_release=self.download)
        self.progress_bar = MDProgressBar(value=0, max=100)
        # Adding widgets to the main layout
        layout.add_widget(h_layout)
        layout.add_widget(download_button)
        layout.add_widget(self.progress_bar)

        return layout

    def download(self, instance):
        # Get the URL from the TextField
        url = self.url_input.text
        print(f"Downloading from {url}")
        # You can add the logic to download from the URL here
        cl = Client(language="en")
        #video = cl.get(str(url))
        self.choose_file()
        #video.download(path=self.path, quality=Quality.BEST, display=self.update_progress)

    def update_progress(self, pos, total):
        # Update the ProgressBar value based on the pos and total values
        self.progress_bar.value = (pos / total) * 100


    def choose_file(self):
        filechooser.open_file(on_selection=self.selected)

    def selected(self, selection):
        self.path = selection


if __name__ == "__main__":
    DownloadApp().run()

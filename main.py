import kivy.utils
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.textfield import MDTextField
from kivy.uix.progressbar import ProgressBar
from threading import Thread
from kivy.core.clipboard import Clipboard
import os
from phub import Client, Quality

if kivy.utils.platform == "android":
    from android.permissions import request_permissions, Permission # Only available at runtime on Android


KV = '''
BoxLayout:
    orientation: 'vertical'

    BoxLayout:
        MDLabel:
            text: "Enter URL:"
        MDTextField:
            id: url_input
        MDFlatButton:
            text: "Paste"
            on_release: app.paste_clipboard()

    BoxLayout:
        MDLabel:
            text: "Output Location:"
        MDTextField:
            id: output_input
        MDFlatButton:
            text: "Choose Directory"
            on_release: app.file_manager_open()

    MDFlatButton:
        text: "Download"
        on_release: app.start_download_thread()

    ProgressBar:
        id: progress_bar
        max: 100
'''


class DownloadApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Purple'
        request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
        return Builder.load_string(KV)


    def paste_clipboard(self):
        self.root.ids.url_input.text = Clipboard.paste()

    def file_manager_open(self):
        home_dir = "/storage/emulated/0/"
        self.file_manager = MDFileManager(exit_manager=self.exit_manager,
                                          select_path=self.select_path)
        self.file_manager.show(home_dir)

    def select_path(self, path):
        self.exit_manager()
        self.root.ids.output_input.text = path

    def exit_manager(self, *args):
        self.file_manager.close()

    def start_download_thread(self):
        download_thread = Thread(target=self.download)
        download_thread.start()

    def download(self):
        # Assuming you have the Client class and related methods defined somewhere
        cl = Client(language="en", delay=False)
        video = cl.get(self.root.ids.url_input.text)
        video.download(quality=Quality.BEST, path=self.root.ids.output_input.text, callback=self.update_progress)

    def update_progress(self, pos, total):
        self.root.ids.progress_bar.value = (pos / total) * 100


if __name__ == '__main__':
    DownloadApp().run()

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
<ContentNavigationDrawer>:

    ScrollView:

        MDList:

            OneLineListItem:
                text: "Screen 1"
                on_press:
                    root.nav_drawer.set_state("close")
                    app.screen_manager.current = "scr 1"

            OneLineListItem:
                text: "Screen 2"
                on_press:
                    root.nav_drawer.set_state("close")
                    app.screen_manager.current = "scr 2"

Screen:

    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 10
        title: "Downloader App"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

    MDNavigationLayout:
        x: toolbar.height

        ScreenManager:
            id: screen_manager

            Screen:
                name: "scr 1"

                BoxLayout:
                    orientation: 'vertical'

                    MDTextField:
                        id: url_input
                        hint_text: "Enter URL"
                        helper_text: "Paste the video URL you want to download"
                        helper_text_mode: "on_focus"

                    BoxLayout:
                        orientation: 'horizontal'
                        adaptive_size: True
                        padding: "10dp"

                        MDFlatButton:
                            text: "Paste"
                            on_release: app.paste_clipboard()

                        MDFlatButton:
                            text: "Choose Directory"
                            on_release: app.file_manager_open()

                    MDFlatButton:
                        text: "Download"
                        on_release: app.start_download_thread()

                    ProgressBar:
                        id: progress_bar
                        max: 100

    MDNavigationDrawer:
        id: nav_drawer

        ContentNavigationDrawer:
            screen_manager: screen_manager
            nav_drawer: nav_drawer
'''


class DownloadApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Purple'  # Set the primary color
        self.theme_cls.accent_palette = 'Amber'  # Set the accent color
        self.theme_cls.theme_style = "Light"  # "Dark" for dark theme
        if kivy.utils.platform == "android":
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

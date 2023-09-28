import kivy.utils
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.textfield import MDTextField
from kivymd.uix.toolbar import MDTopAppBar # Ensure MDToolbar is imported
from kivymd.uix.navigationdrawer import MDNavigationLayout, MDNavigationDrawer
from kivymd.uix.list import OneLineListItem
from kivy.uix.screenmanager import ScreenManager, Screen
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
    padding: dp(10)
    spacing: dp(10)

    BoxLayout:
        spacing: dp(10)

        MDLabel:
            text: "Enter URL:"
            theme_text_color: "Secondary"
            
        MDTextField:
            id: url_input
            md_bg_color: app.theme_cls.primary_light
            elevation: 8
            radius: [dp(10)]
            
        MDRaisedButton:
            text: "Paste"
            md_bg_color: app.theme_cls.primary_color
            elevation: 8
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            on_release: app.paste_clipboard()
            radius: [dp(10)]

    BoxLayout:
        spacing: dp(10)

        MDLabel:
            text: "Output Location:"
            theme_text_color: "Secondary"
            
        MDTextField:
            id: output_input
            md_bg_color: app.theme_cls.primary_light
            elevation: 8
            radius: [dp(10)]
            
        MDRaisedButton:
            text: "Set Path"
            md_bg_color: app.theme_cls.primary_color
            elevation: 8
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            on_release: app.file_manager_open()
            radius: [dp(10)]

    MDRaisedButton:
        text: "Download"
        md_bg_color: app.theme_cls.primary_color
        elevation: 8
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        on_release: app.start_download_thread()
        radius: [dp(10)]

    ProgressBar:
        id: progress_bar
        max: 100
        background_color: app.theme_cls.primary_light
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

# Coded entirely by ChatGPT
# Used for v0.2
# Release v0.3 will be written by myself (Kivy is not so intuitive for me, so please be patient)

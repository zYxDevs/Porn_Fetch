from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.filemanager import MDFileManager
import os

KV = """
BoxLayout:
    orientation: 'vertical'
    padding: '10dp'
    spacing: '10dp'

    MDRaisedButton:
        text: "Open File Dialog"
        on_release: app.open_file_dialog()
"""


class FileDialogApp(MDApp):
    def build(self):
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
        )
        return Builder.load_string(KV)

    def open_file_dialog(self):
        # Open the file manager in the main thread
        self.file_manager.show('/')  # Show file manager from the root directory

    def select_path(self, path):
        # Callback for when a file/directory is selected
        directory = os.path.dirname(path)
        popup = Popup(title='Selected File and Directory',
                      content=Label(text=f"File: {path}\nDirectory: {directory}"),
                      size_hint=(None, None), size=(400, 400))
        popup.open()
        self.exit_manager()

    def exit_manager(self, *args):
        # Close the file manager
        self.file_manager.close()


if __name__ == '__main__':
    FileDialogApp().run()


## I am jumping from the bridge if that shit doesn't work... (Joke)
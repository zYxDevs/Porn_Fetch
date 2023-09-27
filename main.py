from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from plyer import filechooser

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
        return Builder.load_string(KV)

    def open_file_dialog(self):
        # Open the file dialog in the main thread
        filechooser.choose_dir(on_selection=self.selected)

    def selected(self, selection):
        if selection:
            selected_path = selection[0]
            popup = Popup(title='Selected Directory',
                          content=Label(text=selected_path),
                          size_hint=(None, None), size=(400, 400))
            popup.open()
        else:
            popup = Popup(title='No Directory Selected',
                          content=Label(text='No directory was selected!'),
                          size_hint=(None, None), size=(400, 400))
            popup.open()


if __name__ == '__main__':
    FileDialogApp().run()

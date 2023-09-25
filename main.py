import os
import sys
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.uix.button import Button
from kivy.lang import Builder
from plyer import filechooser



try:
    import phub

except Exception as e:
    exception = e


class MainApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return self.choose_file()

    def choose_file(self):
        filechooser.open_file(on_selection=self.selected)

    def selected(self, selection):
        print(selection)




MainApp().run()
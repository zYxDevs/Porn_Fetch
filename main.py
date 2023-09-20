from kivy.app import App
from kivy.utils import platform
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.progressbar import ProgressBar
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from threading import Thread
from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.theming import ThemeManager

if platform == "android":
    try:
        from jnius import autoclass
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        Permission = autoclass('android.Manifest$permission')
        ActivityCompat = autoclass('androidx.core.app.ActivityCompat')
        ContextCompat = autoclass('androidx.core.content.ContextCompat')

    except Exception as e:
        exception = True
        text = str(e)

try:
    import phub
    text = """Enter URL here:"""
    exception = False

except Exception as e:
    exception = True
    text = f"There was an error importing phub. Please report the following: {e}"


def strip_tittle(title):
    control_chars = ''.join(chr(i) for i in range(32))
    special_chars = '/\\?<>:*|&"$%!;\'#'
    all_special_chars = list(control_chars + special_chars)

    for special_char in all_special_chars:
        title = str(title).strip(special_char)

    return title




class MyBoxLayout(BoxLayout):

    if platform == "android":
        def build(self):
            self.request_android_permissions()

        def have_permission(self, perm):
            activity = PythonActivity.mActivity
            return ContextCompat.checkSelfPermission(activity, perm) == 0

        def request_android_permissions(self):
            activity = PythonActivity.mActivity

            if not self.have_permission(Permission.WRITE_EXTERNAL_STORAGE):
                ActivityCompat.requestPermissions(activity, [Permission.WRITE_EXTERNAL_STORAGE], 1234)

            if not self.have_permission(Permission.READ_EXTERNAL_STORAGE):
                ActivityCompat.requestPermissions(activity, [Permission.READ_EXTERNAL_STORAGE], 1235)

    def __init__(self, **kwargs):
        super(MyBoxLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = "10dp"
        self.spacing = "10dp"
        self.c = phub.Client(language="en")

        self.url_input = MDTextField(
            hint_text=str(text),
            mode="rectangle",
            size_hint_y=None,
            height="40dp"
        )
        self.add_widget(self.url_input)

        if platform == "android":
            environment = autoclass('android.os.Environment')
            self.download_folder = environment.getExternalStoragePublicDirectory(
                environment.DIRECTORY_DOWNLOADS).getAbsolutePath()

        else:
            self.download_folder = "./"

        information = MDTextField(
            hint_text=str(f"Output folder: {self.download_folder}"),
            mode="rectangle",
            size_hint_y=None,
            height="40dp",
            readonly=True
        )
        self.add_widget(information)

        self.submit_button = MDRaisedButton(
            text='Download Video',
            pos_hint={'center_x': 0.5}
        )
        self.submit_button.bind(on_press=self.download_video)
        self.add_widget(self.submit_button)

        self.progress_bar = ProgressBar(max=100, size_hint_y=None, height="30dp")
        self.add_widget(self.progress_bar)

    def show_popup(self, title, message):
        dialog = MDDialog(
            title=title,
            text=message,
            buttons=[MDRaisedButton(text="Close", on_release=self.close_dialog)]
        )
        dialog.open()

    def close_dialog(self, instance):
        instance.parent.dismiss()

    def download_video(self, instance):
        download_thread = Thread(target=self.raw_download)
        download_thread.start()

    def raw_download(self):
        try:

            url = self.url_input.text
            video = self.c.get(url)
            path = self.download_folder
            quality = phub.Quality.BEST
            video.download(path=path, quality=quality, callback=self.update_progress)

        except Exception as exc:
            error_details = f"{type(exc).__name__}: {str(exc)}"
            Clock.schedule_once(lambda dt, err=error_details: self.show_popup("Error", err))

    def update_progress(self, pos, total):
        percentage_complete = (pos / total) * 100
        Clock.schedule_once(lambda dt: setattr(self.progress_bar, 'value', percentage_complete))


class MyApp(MDApp):
    theme_cls = ThemeManager()

    def build(self):
        self.theme_cls.primary_palette = "Blue"  # Change this for a different color
        return MyBoxLayout()


if __name__ == '__main__':
    MyApp().run()

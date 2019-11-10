from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import (FadeTransition, Screen, ScreenManager,
                                    ShaderTransition)
from kivy.uix.widget import Widget


class PrivacyApp(App):
    def build(self):
        self.title = "Your Privacy on Social Platforms"
        return sm

Builder.load_file("layout.kv")


class Main_Window(Screen):
    pass


class Facebook_Window(Screen):
    pass


class FacebookPI_Window(Screen):
    pass


class Instagram_Window(Screen):
    pass


class InstagramPI_Window(Screen):
    pass


class Twitter_Window(Screen):
    pass


class TwitterPI_Window(Screen):
    pass

class LinkedIn_Window(Screen):
    pass


class LinkedInPI_Window(Screen):
    pass

class Snapchat_Window(Screen):
    pass

class SnapchatPI_Window(Screen):
    pass

sm = ScreenManager(transition=FadeTransition(clearcolor=[0, 0, 0, 1]))

screens = [Main_Window(name="main"),
           Facebook_Window(name="facebook"),
           FacebookPI_Window(name="facebookpi"),
           Instagram_Window(name="instagram"),
           InstagramPI_Window(name="instagrampi"),
           Twitter_Window(name="twitter"),
           TwitterPI_Window(name="twitterpi"),
           LinkedIn_Window(name="linkedin"),
           LinkedInPI_Window(name='linkedinpi'),
           Snapchat_Window(name="snapchat"),
           SnapchatPI_Window(name='snapchatpi')]

for screen in screens:
    sm.add_widget(screen)

sm.current = "main"

if __name__ == '__main__':
    PrivacyApp().run()

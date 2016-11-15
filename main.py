import kivy
kivy.require('1.9.1') # replace with your current kivy version !

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

Builder.load_file('featrainer.kv')

class AppScreenManager(ScreenManager):
    def __init__(self, initial_screen, **kwargs):
        super(AppScreenManager, self).__init__(**kwargs)

        self.switch_to(initial_screen)

class InitialScreen(Screen):
    def __init__(self, **kwargs):
        super(InitialScreen, self).__init__(**kwargs)

        self.welcome_window = WelcomeWindow()
        self.add_widget(self.welcome_window)



class WelcomeWindow(BoxLayout):
    def __init__(self, **kwargs):
        super(WelcomeWindow, self).__init__(**kwargs)

        widgets = []

        #self.Label1 = Label(text='text 1')
        #self.Label2 = Label(text='text 2')
        #self.Label3 = Label(text='text 3')

        #self.add_widget(self.Label1)
        #self.add_widget(self.Label2)
        #self.add_widget(self.Label3)



class IntroductionScreen(Screen):
    def __init__(self, **kwargs):
        super(IntroductionScreen, self).__init__(**kwargs)

        #self.introduction_screen = WelcomeWindow()
        #self.add_widget(self.welcome_window)

class MyApp(App):

    def build(self):
        self.screen_dict = {
            'initial' : InitialScreen,
            'introduction' : IntroductionScreen
        }

        # let's register screen classes addresses to the main app
        for (shortname_index, screen_class) in self.screen_dict.items():
            setattr(self, screen_class.__name__, screen_class)

        self.AppScreenManager = AppScreenManager(initial_screen=InitialScreen())
        return self.AppScreenManager

    #def show_IntroductionScreen(self):
    #    self.AppScreenManager.switch_to(IntroductionScreen())

    def showScreen(self, screen='initial', **kwargs):

        self.AppScreenManager.switch_to(self.screen_dict[screen]())
        #return list[screen]


if __name__ == '__main__':
    MyApp().run()

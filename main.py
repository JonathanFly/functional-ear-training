import kivy
kivy.require('1.9.1') # replace with your current kivy version !

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.rst import RstDocument
from kivy.uix.screenmanager import FadeTransition, NoTransition

Builder.load_file('featrainer.kv')

class AppScreenManager(ScreenManager):
    def __init__(self, initial_screen, **kwargs):
        super(AppScreenManager, self).__init__(**kwargs)

        self.switch_to(initial_screen)

class InitialScreen(Screen):
    def __init__(self, **kwargs):
        super(InitialScreen, self).__init__(**kwargs)

class IntroductionScreen(Screen):
    def __init__(self, **kwargs):
        super(IntroductionScreen, self).__init__(**kwargs)

    def getDocument(self):

        try:
            document = str(open('text_test.rst','r').read())
            self.document = document
        except FileNotFoundError:
            self.document = 'Documentation not Found; please check your installation.'

        return self.document

class BasicScreen(Screen):
    def __init__(self, **kwargs):
        super(BasicScreen, self).__init__(**kwargs)


class ExerciseListScreen(Screen):
    def __init__(self, **kwargs):
        super(ExerciseListScreen, self).__init__(**kwargs)

class MyApp(App):

    def build(self):

        # this will be set when screen change needs confirmation
        self.is_occupied = False

        self.screen_dict = {
            'initial' : InitialScreen,
            'introduction' : IntroductionScreen,
            'basic' : BasicScreen,
        }

        # let's register screen classes addresses to the main app
        for (shortname_index, screen_class) in self.screen_dict.items():
            setattr(self, screen_class.__name__, screen_class)

        self.AppScreenManager = AppScreenManager(initial_screen=InitialScreen(), transition=kivy.uix.screenmanager.NoTransition())
        return self.AppScreenManager

    def showScreen(self, screen='initial', **kwargs):

        self.AppScreenManager.switch_to(self.screen_dict[screen]())


if __name__ == '__main__':
    MyApp().run()

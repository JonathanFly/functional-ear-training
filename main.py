import kivy
kivy.require('1.9.1') # replace with your current kivy version !

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.rst import RstDocument
from kivy.uix.screenmanager import FadeTransition, NoTransition
from kivy.properties import StringProperty

from configobj import ConfigObj

Builder.load_file('featrainer.kv')

class AppHeader(BoxLayout):

    screen_title = StringProperty()

    def __init__(self, screen_title='', **kwargs):
        super(AppHeader, self).__init__(**kwargs)
        self.screen_title = screen_title

    def get_screen_title(self):
        return self.screen_title

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
    def __init__(self, exercise, **kwargs):
        super(ExerciseListScreen, self).__init__(**kwargs)

        exercises = ConfigObj('exercises/{}.fetl'.format(exercise))

        self.ids.app_header.screen_title = 'hey'

        for section in exercises.sections:
            test_button = Button(text=exercises[section]['title'])
            self.ids.exercise_list_grid.add_widget(test_button)


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

    def showExerciseListScreen(self, exercise):

        self.ExerciseListScreen = ExerciseListScreen(exercise)
        self.AppScreenManager.switch_to(self.ExerciseListScreen)


if __name__ == '__main__':
    MyApp().run()

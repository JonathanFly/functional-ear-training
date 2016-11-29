import kivy
kivy.require('1.9.1') # replace with your current kivy version !

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.text.markup import MarkupLabel
from kivy.uix.rst import RstDocument
from kivy.uix.screenmanager import FadeTransition, NoTransition
from kivy.properties import StringProperty, ObjectProperty
#from kivy.uix.settings import Settings, SettingsPanel
import kivy.uix.settings as kset

from configobj import ConfigObj

from midi2audio import FluidSynth

Builder.load_file('featrainer.kv')

class AppScreenManager(ScreenManager):
    def __init__(self, initial_screen, **kwargs):
        super(AppScreenManager, self).__init__(**kwargs)

        self.switch_to(initial_screen)

class AppHeader(BoxLayout):

    screen_title = StringProperty()

    def __init__(self, screen_title='', **kwargs):
        super(AppHeader, self).__init__(**kwargs)
        self.screen_title = screen_title

    def get_screen_title(self):
        return self.screen_title

class ExerciseHeader(BoxLayout):

    screen_title = StringProperty()

    def __init__(self, screen_title='', **kwargs):
        super(ExerciseHeader, self).__init__(**kwargs)
        self.screen_title = screen_title

    def get_screen_title(self):
        return self.screen_title


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
            config_dict = exercises[section].dict()
            test_button = ExerciseButton(config_dict=config_dict,text=self.bt_text(config_dict['title']), markup=True, valign='top', halign='center')

            self.ids.exercise_list_grid.add_widget(test_button)

    def bt_text(self, ex_title):
        hey = str()
        for idx,item in enumerate(ex_title):
            if idx==0:
                hey += "[size=19]{}[/size]\n".format(item)
            elif idx==1:
                hey += "[b]{}[/b]\n".format(item)
            elif idx==2:
                hey += "{}\n".format(item)

        return hey

        #def bt_callback(self, instance):

class ExerciseButton(Button):

    config_dict = ObjectProperty()

    def __init__(self, config_dict=config_dict, **kwargs):
        super(ExerciseButton, self).__init__(**kwargs)
        self.config_dict = config_dict

class ExerciseLoadWidget(BoxLayout):
    def __init__(self, config_dict=None, **kwargs):
        super(ExerciseLoadWidget, self).__init__(**kwargs)

        #self.ids.exercise_container.add_widget(ExerciseLoadPlayWidget)

class ExercisePlayWidget(BoxLayout):
    def __init__(self, config_dict=None, **kwargs):
        super(ExercisePlayWidget, self).__init__(**kwargs)

        #self.ids.exercise_container.add_widget(ExerciseLoadPlayWidget)

class ExerciseScreen(Screen):
    def __init__(self, config_dict=None, **kwargs):
        super(ExerciseScreen, self).__init__(**kwargs)

        self.ids.exercise_container.add_widget(ExerciseLoadWidget(config_dict))

class SettingsWidget(kset.InterfaceWithNoMenu):
    def __init__(self, **kwargs):
        super(SettingsWidget, self).__init__(**kwargs)

        #mabudddy = kset.SettingsPanel(title='hello mate')

        maopts= [
                     "Numbers",
                     "Letters",
                     "Movable Do (recommended)",
                     "Movable Do La Minor",
                     "Note Names"
                 ],
        pan = kset.SettingsPanel(title="hello")
        pan.add_widget(kset.SettingTitle(title="HEY BUDDY"))
        #pan.add_widget(kset.SettingOptions(options=maopts, panel=pan))
        self.add_widget(pan)

        #self.add_widget(mabuddy)
        #from kivy.uix.colorpicker import ColorPicker
        #self.register_type('colorpicker', ColorPicker)
            # from kivy.config import ConfigParser
            # from json import dumps
            #
            # global_settings_dict = ConfigObj('settings.cfg')
            #
            # config_dict = [
            #     {
            #         "type" : "title",
            #         "title" : "Settings"
            #     },
            #     {
            #         "type" : "options",
            #         "title" : "Buttons Labels",
            #         "options" : [
            #             "Numbers",
            #             "Letters",
            #             "Movable Do (recommended)",
            #             "Movable Do La Minor",
            #             "Note Names"
            #         ],
            #         "section" : "buttonslabels",
            #         "key" : "buttonslabels"
            #     },
            # ]
            #
            # config_json = dumps(config_dict)
            # config = ConfigParser()
            # config.read(config_json)
            #
            # config.setdefault("buttonslabels","buttonslabels", "Movable Do (recommended)")
            #
            # returning_json = str()
            #
            # print(config_json)
            # s = Settings()
            # s.create_json_panel("Buttons Labels", config, data=config_json)
            # self.ids.settings_container.add_widget(s)

            #print(returning_json)

class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)
        self.add_widget(SettingsWidget())

class MyApp(App):

    def build(self):

        # this will be set when screen change needs confirmation
        self.is_occupied = False

        self.screen_dict = {
            'initial' : InitialScreen,
            'introduction' : IntroductionScreen,
            'basic' : BasicScreen,
            'settings' : SettingsScreen,
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

    def showExercise(self, config_dict):

        self.ExerciseScreen = ExerciseScreen(config_dict)
        self.AppScreenManager.switch_to(self.ExerciseScreen)


if __name__ == '__main__':
    MyApp().run()

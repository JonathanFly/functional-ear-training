from configobj import ConfigObj

class ExerciseList:
    def __init__(self, exercise=None, exerciselist_cfg=None):
        pass

    def returnList(self):
        pass

class ExerciseBase:

    def __init__(self, settings_dict=None, filename=None, configobj_str=None):
        self.settings = ExerciseSettings(settings_dict=config_dict)

class Exercise(ExerciseBase):

    def __init__(self, config_dict, **kwargs):
        super(Exercise, self).__init__(**kwargs)

        self.s = ExerciseSettings(config_dict=config_dict)
        #self.settings = ExerciseSettings(settings_dict=config_dict)

class ExerciseSettings:

    def __init__(self, settings_dict=None, filename=None, configobj_str=None):

        if settings_dict:
            s = settings_dict
        elif filename:
            s = ConfigObj(filename)
        elif configobj_str:
            s = ConfigObj(configobj_str)

        self.s = s

        print(s['title'])

        for key, value in s.items():
            setattr(self, key, value)

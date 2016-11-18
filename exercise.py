from configobj import ConfigObj

class ExerciseList:
    def __init__(self, exercise=None, exerciselist_cfg=None):
        pass

    def returnList(self):
        pass

class ExerciseBase:

    def __init__(self, filename=None, configobj_str=None, settings_dict=None):
        pass

class ExerciseSettings:

    def __init__(self, filename=None, configobj_str=None, settings_dict=None):

        if filename:
            s = ConfigObj(filename)
        elif configobj_str:
            s = ConfigObj(configobj_str)
        elif settings_dict:
            s = settings_dict

        self.s = s

        print(s['title'])

        for key, value in s.items():
            setattr(self, key, value)

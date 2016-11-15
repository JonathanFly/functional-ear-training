# Functional Ear Training Design

### frontent

#### root window

*(well designed please)*

* LOGO
* INTRODUCTION
  Basic music info and how the method works
* MODES
  So we don't break things if we add more modes later.
  * Melodic Interval
    * The Major Scale
    * The Minor Scale
    * Chromatics in a Major Context
    * Chromatics in a Minor Context
  * Melodic dictation
  * (*new ones*? great.)
* SETTINGS
  Is better to put it in root window/menu, so that we organize it comprehensively.
  * Melodic Interval
  * Melodic dictation

### backend

* dict settingsDict
  * *cadence*
    * I-IV-V-I (default)
    * V7-V7-V7-V7-1
    * I-IV-V-I
    * I
    * tonic
  * *cadence tempo*
    * default: 90bpm
    * min: 40bpm
    * max: 280bpm
  * *resolution*
    * Original (default)
    * Alternative
    * 5 -> 1  
* class ExerciseBase
  * *properties:*
    * number of questions (default: 20; min: 10, max: 100)
    * key type (major/minor)
    * tonic (C, not-C, Random)
    * many octaves (boolean)
    * chromatics (boolean)
    * enables tones (1,b2,2,b3,3,4,#4,5,b6,6,b7,7,1)
* class MelodicInterval(subclasses ExerciseBase)
* class MelodicDictation(subclasses ExerciseBase)

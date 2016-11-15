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
  These are mainly global (default *settingsDict* or specific *settingsDict* for custom exercise)

### backend

* dict settingsDict
  * *buttonslabels*
    * Numbers
    * Letters
    * Movable Do (recommended)
    * Movable Do La minor
    * Note names
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
  * *playcadence*
    * Always (beginners)
    * Every 5 Questions
    * Once for a new key
    * Never
  * *aftercorrectanswer*
    * Play resolution (beginners)
    * Play the correct tone
    * Just indicate the correct tone
    * *pause*
      * default: 0.5 (in seconds; min: 0, max: 3.0)
  * *whengivingup*
    * playcadence  (boolean)
    * *aftercadence*:
      * play resolution (beginners)
      * play correct tone ()
  * *notes tempo*
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

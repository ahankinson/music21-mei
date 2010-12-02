""" Designed to be plugged into the Music21 converter system. """
from pymei.Import import convert
from pymei.Helpers import flatten
from music21 import stream
from music21 import bar
from music21 import meter
from music21 import key
from music21 import note
from music21 import duration
from music21 import spanner

import logging
import pprint
lg = logging.getLogger('pymei')
"""
    Score -> stream.Score():
        Staff Group -> spanner.StaffGroup()
            Staves -> spanner.Staff():
                Parts -> stream.Part():
                    Measures -> stream.Measure():
                        Notes -> note.Note()
                        Rests -> note.Rest()
                        Dynamics -> dynamics.Dynamic()

"""


class ConverterMeiError(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return repr(self.message)

class ConverterMei(object):
    def __init__(self):
        self._meiDoc = None
        self._score = stream.Score()
        self._sections = {}
        self._score_defs = []
        
        self._currentTimeSig = None # time signatures can change. This is the current one.
        self._timeSigHasChanged = False # set this to true if we hit a tsig change
        self._currentKeySig = None # key sigs can change. This is the current one.
        self._keySigHasChanged = False # set this to true if we hit a ksig change
        
        # This will be different for each voice. We may want to look for a better
        # place to track this.
        self._currentClef = None
        self._clefHasChanged = False
        
        self._staves = {} # {staffnum: <m21 staff object>}
        
        self.__flat_score = None # the flattened objects in the score.
        
    
    def parseFile(self, fn):
        self._meiDoc = convert(fn)
        self._firstPass()
        self._secondPass()
        
        #self._score.append(self._staves.values())
        
        #self._score.show('text')
        pass
    
    def _firstPass(self):
        """ 
            Work out what the sections and global values are we need, and 
            set us up the score.
        """
        
        self.__flat_score = flatten(self._meiDoc.search('score')[0])
        score_elements = (
            'scoredef',
            'staffdef',
            'layerdef',
            'instrdef',
        )
        self._score_defs = filter(lambda s: s.name in score_elements, self.__flat_score)
        lg.debug("Score Definitions: ".format(pprint.pprint(self._score_defs)))
        
        # set some defaults based on the scoredef header section
        sc = filter(lambda s: s.getname() == 'scoredef', self._score_defs)[0]
        
        mc = sc.attribute_by_name('meter.count').value
        mu = sc.attribute_by_name('meter.unit').value
        self._currentTimeSig = meter.TimeSignature()
        self._currentTimeSig.load("{0}/{1}".format(mc, mu))
        
        ks = self._keysigConverter(sc.attribute_by_name('key.sig').value)
        self._currentKeySig = key.KeySignature(ks)
        
        sections = filter(lambda s: s.name == "section", self.__flat_score)
        section_elements = (
            'scoredef',
            'measure',
            'staff',
            'layer',
            'note',
            'rest',
            'mrest',
            'beam',
            'dynam',
            'slur',
            'hairpin',
            'fermata',
            'mordent'
        )
        
        # we don't need to encode sections, but having them sorted here makes it pretty
        # handy to work with them.
        for section in sections:
            se = filter(lambda s: s.name in section_elements, flatten(section))
            self._sections[section] = se
        lg.debug("Section elements: {0}".format(pprint.pprint(self._sections)))
        
        # 
        # lg.debug("Staves: {0}".format(self._staves))
        
    def _secondPass(self):
        # this is where it goes all squirrely. In MEI, measures are parents of voices
        # in Music21, parts are parents of measures. This simple fact keeps me up at night.
        
        # 1. Get staff definitions, if they exist.
        
        # 2. Something.
        
        # 3. Once we have all the staves identified, find out, for each one, how many
        #  voices ("layers") they have.
        
        # 4. If the staff already has a part defined with the same ID, that's OK; otherwise
        #  add a new voice ("part") to the staff.
        
        # 5. Now we can parse the sections. Get the section stuff that we parsed earlier
        #  and iterate through them.
        
        # 6. In this section, see if we have a scoredef as the first element. If so, trigger some
        #  of the state changes if we do so we can apply that to the measure creation.
        
        # 7. For all the layers in this section, grab the previously defined part on this staff
        #  in this MEI measure.
        
        # 8. Add the notes to the measure.
        
        # 9. Add the measure to the part
        
        # 10. Add the part to the staff (?)
        
        # 11. Add the staff to the staff group
        
        # 12. Add the staff group to the score.
        pass
    
    def _thirdPass(self):
        # This goes through and looks for "spanner" elements like slurs, ties, triplets,
        # etc. When it finds one, it adds it to the appropriate element.
        pass
    
    
    def _calculateParts(self, section):
        # we need to find out how many parts are in this section.
        
    
    def _createMeasure(self, measure_element):
        m_measure = stream.Measure()
        if measure_element.has_attribute('n') and measure_element.measure_number.isdigit():
            m_measure.number = int(measure_element.measure_number)
        
        if measure_element.has_barline:
            if not measure_element.is_repeat:
                m_barline = bar.Barline()
                m_barline.style = self._barlineConverter(measure_element.barline)
            else:
                m_barline = bar.Repeat()
                m_barline.style = self._barlineConverter(measure_element.barline)
                if measure_element.barline is "rptstart":
                    m_barline.direction = "start"
                elif measure_element.barline is "rptend":
                    m_barline.direction = "end"
            m_measure.rightBarline = m_barline
        
        # change triggers.
        if self._timeSigHasChanged:
            m_measure.timeSignatureIsNew = True
            m_measure.timeSignature = self._currentTimeSig
            self._timeSigHasChanged = False
        
        if self._keySigHasChanged:
            m_measure.keyIsNew = True
            m_measure.keySignature = self._currentKeySig
            self._keySigHasChanged = False
        
        if self._clefHasChanged:
            m_measure.clefIsNew = True
            m_measure.clef = self._currentClef
            self._clefHasChanged = False
        
        return m_measure
    
    def _createNote(self, note_element):
        # create a new m21 note
        m_note = note.Note(note_element.get_pitch_octave())
        
        if note_element.has_attribute('dur'):
            # so many duration notations!
            normalized_duration = duration.typeFromNumDict[int(note_element.duration)]
            m_note.duration = duration.Duration(normalized_duration)
            if note_element.is_dotted:
                m_note.duration.dots = int(note_element.dots)
        return m_note
    
    def _barlineConverter(self, barline):
        """ 
            Converts a MEI barline representation into a Music21 and thus a 
            MusicXML barline representation.
        """
        barline_dict = {
            'dashed': 'dashed',
            'dotted': 'dotted',
            'dbl': 'light-light',
            'dbldashed': '',
            'dbldotted': '',
            'end': 'light-heavy',
            'invis': 'none',
            'rptstart': 'heavy-light',
            'rptboth': '',
            'rptend': 'light-heavy',
            'single': ''
        }
        if barline in barline_dict.keys():
            return barline_dict[barline]
        else:
            # should this return empty, or raise an exception? Inquiring minds
            # want to know!
            return ''
        
    
    def _keysigConverter(self, mei_ksig):
        """ 
            Converts a MEI key signature (e.g. 4f, 5s) to absolute circle-of-fifths 
            representation (-/+, e.g. -1 = 1f; +1 = 1s)
        """
        if not mei_ksig[0].isdigit():
            raise ConverterMeiError("Only key signatures with the form <num><str> are supported, e.g. 0, 4f, 5s.")

        if mei_ksig is "0":
            return int(mei_ksig)
        if mei_ksig.endswith("f"):
            return -int(mei_ksig[0])
        return int(mei_ksig[0])


if __name__ == "__main__":
    from optparse import OptionParser
    p = OptionParser()
    p.add_option("-f", "--file", action="store", help="Mei file to test.")
    (options,args) = p.parse_args()

    c = ConverterMei()
    c.parseFile(options.file)
    c._score.show('text')

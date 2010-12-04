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
from music21 import chord
from music21 import beam
from music21 import dynamics
from music21 import expressions

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
        self._object_registry = {}
        
        
        self._currentTimeSig = None # time signatures can change. This is the current one.
        self._timeSigHasChanged = False # set this to true if we hit a tsig change
        self._currentKeySig = None # key sigs can change. This is the current one.
        self._keySigHasChanged = False # set this to true if we hit a ksig change
        
        # This will be different for each voice. We may want to look for a better
        # place to track this.
        self._currentClef = None
        self._clefHasChanged = False
        
        self._parts = {} # {sid-nid: <m21 Part>}
        
        self.__flat_score = None # the flattened objects in the score.
        
    
    def parseFile(self, fn):
        self._meiDoc = convert(fn)
        self._createRegistries()
        
        #self._score.append(self._staves.values())
        
        #self._score.show('text')
        pass
    
    def _createRegistries(self):
        # creates a couple registries for lookups.
        # object-registry:
        #  { element.id: <Music21 Object> }
        #  where element.id is the XML/MEI xml:id, and the corresponding Music21 object.
        #
        # staff-part registry:
        #  {secnum-sid-lid: <Music21 Part> }
        # where secid-sid-lid is the section number, staff number and layer number used
        # as a lookup for a part. If that does not exist, a new part is created.
        
        #==== object registry
        self.__flat_score = flatten(self._meiDoc.search('music')[0])
        
        elements_to_convert = (
            'note',
            'measure',
            'chord',
            'fermata',
            'beam',
            'rest',
            'mrest',
            'slur',
            'tie',
            'trill',
            'hairpin',
        )
        m_obj = filter(lambda c: c.name in elements_to_convert, self.__flat_score)
        
        for el in m_obj:
            if el.name == 'note':
                self._object_registry[el.id] = self._createNote(el)
            elif el.name == 'measure':
                self._object_registry[el.id] = self._createMeasure(el)
            elif el.name == 'chord':
                self._object_registry[el.id] = self._createChord(el)
            elif el.name == 'fermata':
                self._object_registry[el.id] = self._createFermata(el)
            elif el.name == 'beam':
                self._object_registry[el.id] = self._createBeam(el)
            elif el.name in ('rest', 'mrest'):
                self._object_registry[el.id] = self._createRest(el)
            elif el.name == 'slur':
                self._object_registry[el.id] = self._createSlur(el)
            elif el.name == 'tie':
                self._object_registry[el.id] = self._createTie(el)
            elif el.name == 'trill':
                self._object_registry[el.id] = self._createTrill(el)
            elif el.name == 'hairpin':
                self._object_registry[el.id] = self._createHairpin(el)
            
        lg.debug("Object registry: {0}".format(pprint.pprint(self._object_registry)))
        
        
        #==== staff-part registry =====
        sections = self._meiDoc.search('section')
        for secnum, section in enumerate(sections):
            staves = section.descendents_by_name('staff')
            self._sections[secnum] = {}
            
            for staff in staves:
                staffnum = staff.attribute_by_name('n').value
                layers = staff.descendents_by_name('layer')
                
                for layer in layers:
                    laynum = layer.attribute_by_name('n').value
                    pid = "{0}-{1}".format(staffnum, laynum)                    
                    if pid not in self._sections[secnum].keys():
                        self._sections[secnum][pid] = stream.Part()
                        
    def _thirdPass(self):
        # This goes through and looks for "spanner" elements like slurs, ties, triplets,
        # etc. When it finds one, it adds it to the appropriate element.
        pass
    
    
    
    
    def _calculatePart(self, obj):
        # given an object (note, rest, etc.), calculates the part lookup for the staff-part
        # registry lookup.
        # this helps determine which part this object belongs to.
        sn, ln = None
        sn = obj.ancestor_by_name('staff').attribute_by_name('n').value
        ln = obj.ancestor_by_name('layer').attribute_by_name('n').value
        pid = "s{0}-l{1}".format(sn, ln)
    
    def _createBeam(self, beam_element):
        m_beam = beam.Beam()
        # see the music21 beams documentation. This will need to be adjusted
        # to work with "Beams," by getting all the sub-notes and adding them. 
        # But we'll keep it like this for now.
        return m_beam
    
    def _createChord(self, chord_element):
        m_chord = chord.Chord()
        # other stuff.
        return m_chord
    
    def _createRest(self, rest_element):
        m_rest = note.Rest()
        return m_rest
    
    def _createSlur(self, slur_element):
        m_slur = spanner.Slur()
        return m_slur
    
    def _createHairpin(self, hairpin_element):
        m_hairpin = dynamics.Wedge()
        return m_hairpin
    
    def _createFermata(self, fermata_element):
        m_fermata = expressions.Fermata()
        return m_fermata
    
    def _createTrill(self, trill_element):
        m_trill = expressions.Trill()
        return m_trill
        
    def _createTie(self, tie_element):
        m_tie = tie.Tie()
        return m_tie
    
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

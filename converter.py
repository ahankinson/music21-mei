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
from music21 import tie
from music21 import clef

import types
import logging
import pprint
import copy
lg = logging.getLogger('pymei')

# document => stream.Score()
# staff/staffgrp => stream.Part()
# layer => stream.Voice()
# measure => stream.Measure()



class ConverterMeiError(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return repr(self.message)

class ConverterMei(object):
    def __init__(self):
        """docstring for __init__"""
        self._meiDoc = None
        self._sections = None
        self._score = stream.Score()
        self._staff_registry = {}
        self._voice_registry = {}
        self._registry = [] # {id: <m21_obj>}
        
        # these objects have direct mappings from MEI to M21 elements.
        # Thus than can easily be converted and stored for later.
        self._objects_to_convert = {
            'note': self._create_note,
            'rest': self._create_rest,
            'slur': self._create_slur,
            'chord': self._create_chord,
            'mrest': self._create_rest,
            'staffgrp': self._create_staffgrp,
            'staffdef': self._create_staffdef,
            'layerdef': self._create_voice,
            'staff': self._create_staffdef,
            'layer': self._create_voice,
        }
        
        # This holds the a pointer to the music21 object for the contexts
        # we encounter as we parse the file. 
        # This will always hold the most "recent" element
        # that we've encountered, so we can always refer to the context for 
        # the element we need to work on.
        
        # this is useful if, for example, we want to look up what "key signature"
        # context we're currently in, or clef, or measure, or chord, etc.
        self._contexts = {
            'section': None,
            'staff': None,
            'voice': None,
            'note': None,
            'chord': None,
            'measure': None,
            'key_sig': None,
            'time_sig': None,
            'clef': None,
            'beam': None
        }
    
    def parseFile(self, filename):
        """docstring for parseFile"""
        self._meiDoc = convert(filename)
        self._create_registries()
        #self._parse_children(self._meiDoc.gettoplevel())
        self._structure_work()
        lg.debug(self._registry)
    
    # ===============================
    # register objects by ID.
    def _create_registries(self):
        scoredefs = self._meiDoc.search('scoredef')
        for scoredef in scoredefs:
            if not scoredef.ancestor_by_name('section'):
                self._parse_children(scoredef)

        self._sections = self._meiDoc.search('section')
        for section in self._sections:
            if section.descendents_by_name('measure'):
                for measure in section.descendents_by_name('measure'):
                    self._parse_children(measure)
    
    def _parse_children(self, element):
        if element.name in self._objects_to_convert.keys():
            n = self._objects_to_convert[element.name](element)
            if not isinstance(n, types.NoneType):
                self._registry.append((element.id, n))
        if element.children:
            map(self._parse_children, element.children)
            
    # start building the M21 structure
    def _structure_work(self):
        for section in self._sections:
            if section.has_child('scoredef'):
                #set the new scoredefs.
                pass
            self._parse_structure(section)
    
    def _parse_structure(self, element):
        if element.name == "scoredef":
            lg.debug(" ==> Setting a score definition context")
            pass
        elif element.name == "layer":
            lg.debug(" ==> set the layer (voice) context")
            pass
        elif element.name == "staff":
            lg.debug(" ==> setting a staff context")
            pass
        elif element.name == "chord":
            lg.debug(" ==> Setting a chord context")
            pass
        elif element.name == "beam":
            lg.debug(" ==> Setting a beam context")
            pass
        elif element.name == "note"  :
            lg.debug(" ==> Setting a note context ")
            pass
        if element.children:
            map(self._parse_structure, element.children)
    
    def _create_staffgrp(self, element):
        lg.debug("Creating staffgrp from {0}".format(element.id))
        # a staff group will just be a spanner element.
        m_staffgrp = spanner.StaffGroup()
        return m_staffgrp
    
    def _create_measure(self, element):
        # a bit of an anomaly, this one. Since we essentially want to create
        # (part * voice) number of measures, there is not a direct one-to-one
        # mapping of mei measure to m21 measure. Nevertheless, there are certain
        # tasks that we can condense into the measure creation here.
        lg.debug("Creating a measure, for what it's worth, from {0}".format(element.id))
        m_measure = stream.Measure()
        if element.has_attribute('n') and element.measure_number.isdigit():
            m_measure.number = int(element.measure_number)
        
        if element.has_barline:
            if not element.is_repeat:
                m_barline = bar.Barline()
                m_barline.style = self._barline_converter(element.barline)
            else:
                m_barline = bar.Repeat()
                m_barline.style = self._barline_converter(element.barline)
                if element.barline is "rptstart":
                    m_barline.direction = "start"
                elif element.barline is "rptend":
                    m_barline.direction = "end"
                else:
                    raise ConverterMeiError("Could not determine barline type")
            m_measure.rightBarline = m_barline
            
        return m_measure
        
    
    def _create_staffdef(self, element):
        staffnum = element.attribute_by_name('n').value
        if staffnum not in self._staff_registry.keys():
            lg.debug("Creating staffdef from {0}".format(element.id))
            self._staff_registry[staffnum] = stream.Part()
    
    def _create_voice(self, element):
        lid = element.attribute_by_name('n').value
        
        if element.name == "layer":
            sid = element.ancestor_by_name('staff').attribute_by_name('n').value
        elif element.name == "layerdef":
            sid = element.ancestor_by_name('staffdef').attribute_by_name('n').value
        else:
            raise ConverterMeiError("Could not determine voice context.")
        
        address = "{0}.{1}".format(sid, lid)
        if address not in self._voice_registry.keys():
            lg.debug("Creating a new voice from {0}".format(element.id))
            self._voice_registry[address] = stream.Voice()
    
    def _create_note(self, element):
        lg.debug("Creating a note from {0}".format(element.id))
        m_note = note.Note()
        
        return m_note
    
    def _create_rest(self, element):
        lg.debug("Creating a rest from {0}".format(element.id))
        m_rest = note.Rest()
        
        return m_rest
        
    def _create_slur(self, element):
        lg.debug("Creating a slur from {0}".format(element.id))
        m_slur = spanner.Slur()
        
        return m_slur
    
    def _create_chord(self, element):
        lg.debug("Creating a chord from {0}".format(element.id))
        m_chord = chord.Chord()
        
        return m_chord
    
    def _barline_converter(self, barline):
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
            raise ConverterMeiError("Could not convert barline.")

if __name__ == "__main__":
    from optparse import OptionParser
    p = OptionParser()
    p.add_option("-f", "--file", action="store", help="Mei file to test.")
    (options,args) = p.parse_args()

    c = ConverterMei()
    # cProfile.run('c.parseFile(options.file)')
    c.parseFile(options.file)
    # c._score.show('text')
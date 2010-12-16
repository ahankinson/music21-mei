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
        self._score = stream.Score()
        self._staff_registry = {}
        self._voice_registry = {}
        self._registry = [] # {id: <m21_obj>}

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
        
        lg.debug(self._voice_registry)
    
    # ===============================
    def _create_registries(self):
        scoredefs = self._meiDoc.search('scoredef')
        for scoredef in scoredefs:
            if not scoredef.ancestor_by_name('section'):
                self._parse_children(scoredef)

        sections = self._meiDoc.search('section')
        for section in sections:
            if section.has_child('scoredef'):
                # parse the new scoredef.
                pass
            if section.has_child('measure'):
                for measure in section.children_by_name('measure'):
                    self._parse_children(measure)
    
    def _structure_work(self):
        pass
    
    def _parse_children(self, element):
        if element.name in self._objects_to_convert.keys():
            n = self._objects_to_convert[element.name](element)
            self._registry.append((element.id, n))
        if element.children:
            map(self._parse_children, element.children)
    
    def _parse_structure(self, element):
        if element.name == "scoredef":
            lg.debug("Setting a score definition context")
            pass
        elif element.name == "layer":
            lg.debug("set the layer (voice) context")
            pass
        elif element.name == "staff":
            lg.debug("setting a staff context")
            pass
        elif element.name == "chord":
            lg.debug("Setting a chord context")
            pass
        elif element.name == "beam":
            lg.debug("Setting a beam context")
            pass    
        if element.children:
            map(self._parse_structure, element.children)
        
    
    def _create_staffgrp(self, element):
        lg.debug("Creating staffgrp from {0}".format(element.id))
        # a staff group will just be a spanner element.
        m_staffgrp = spanner.StaffGroup()
        return m_staffgrp
    
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

if __name__ == "__main__":
    from optparse import OptionParser
    p = OptionParser()
    p.add_option("-f", "--file", action="store", help="Mei file to test.")
    (options,args) = p.parse_args()

    c = ConverterMei()
    # cProfile.run('c.parseFile(options.file)')
    c.parseFile(options.file)
    # c._score.show('text')
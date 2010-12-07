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

import logging
import pprint
import copy
lg = logging.getLogger('pymei')

class ConverterMeiError(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return repr(self.message)

class ConverterMei(object):
    # =======================
    # Parse order:
    #   1. Score definitions
    #   2. Staff definitions
    #   3. Layer definitions
    #   4. Sections
    #   5. (Score definitions in sections)
    #   6. Measures
    #   7. Staves
    #   8. Layers
    #   9. "Notation Elements":
    #       a. 
    #
    
    def __init__(self):
        self._meiDoc = None
        
        self._score = stream.Score()
        
        # registries
        self._staff_rel_voices = {} # {s1: [v1, v2], s2:[v1]}, etc.
        self._voices_rel_measures = {} # {v1: [m1, m2, m3, m4], v2: [m1, m2, m3, m4]}
        
        self.__flat_score = None
        
        self._num_measures = None
        self._num_sections = None
        self._num_voices = None
        self._num_staves = None
        
        self._registry = {
            'note': self._create_note,
            'measure': self._create_measure,
            'rest': self._create_rest,
            'mrest': self._create_rest,
            'chord': self._create_chord,
            'beam': self._create_beam,
            'staff': self._create_staff,
            'layer': self._create_voice,
            'scoredef': self._create_scoredef,
            'staffgrp': self._create_staffgrp,
            'staffdef': self._create_staffdef,
            'layerdef': self._create_layerdef,
            'verse': self._create_verse,
        }
        
        
    def parseFile(self, fn):
        self._meiDoc = convert(fn)
        self._parse_score()
        pass
        
    # =======================
    def _parse_score(self):
        
        m = self._meiDoc.search('music')
        self.__flat_score = list(flatten(m[0]))
        
        score_iter = copy.copy(self.__flat_score)
        
        for el in score_iter:
            if el.name in self._registry.keys():
                # deal with it
                lg.debug("Dealing with: {0}".format(el.name))
                self._trigger_registry(el)
                
            # else:
            #     lg.debug("Removing: {0}".format(el.name))
            #     self.__flat_score.remove(el)
                
        
        lg.debug("Leftovers: {0}".format(self.__flat_score))
        
        pass
    
    def _trigger_registry(self, element):
        # this method acts as a registry for what to do when
        # an element is encountered. It takes an element as its argument
        # and maps that argument to a method for handling that type of element.
        # 
        # Since elements can exist in many contexts, this was the easiest way
        # to map an element to the appropriate processing instructions.
        if element.name in self._registry.keys():
            m21_obj = self._registry[element.name](element)
            return m21_obj
        else:
            lg.debug("Skipping {0}".format(element.name))
            return None
        
    
    def _create_note(self, mei_element):
        lg.debug("Creating note: {0}".format(mei_element.id))
        m_note = note.Note(mei_element.get_pitch_octave())
        
        if mei_element.duration:
            normalized_duration = self._durationConverter(mei_element.duration)
            m_note.duration = duration.Duration(normalized_duration)
            if mei_element.is_dotted:
                m_note.duration.dots = int(mei_element.dots)
        
        if mei_element.tie:
            # there is no such thing as a medial tie in m21 (yet).
            # we'll define the medial as another start.
            tie_translate = {'i': 'start', 'm':'start', 't': 'end'}
            m_note.tie = tie.Tie(tie_translate[mei_element.tie])
        
        if mei_element.articulations:
            # deal with note articulations.
            pass

        if mei_element.children:
            for child in mei_element.children:
                lg.debug("====>Note Child: {0}".format(child.name))
                if child.name == 'accid':
                    lg.debug("=======>Adding Accidental {0}".format(child.attribute_by_name('accid').value))
                    # self.__flat_score.remove(child)
                elif child.name == 'verse':
                    lg.debug("Processing verse!")
                    vs = self._trigger_registry(child)
                else:
                    lg.debug("Don't know what to do with {0}".format(child.name))
        
        return m_note
                
        
        
    def _create_measure(self, mei_element):
        lg.debug("Creating measure: {0}".format(mei_element.id))
        pass
    
    def _create_rest(self, mei_element):
        lg.debug("Creating rest: {0}".format(mei_element.id))
        pass
    
    def _create_chord(self, mei_element):
        lg.debug("Creating chord: {0}".format(mei_element.id))
        pass
    
    def _create_beam(self, mei_element):
        lg.debug("Creating beam: {0}".format(mei_element.id))
        pass
    
    def _create_staff(self, mei_element):
        lg.debug("Creating staff: {0}".format(mei_element.id))
        pass
    
    def _create_voice(self, mei_element):
        lg.debug("Creating voice: {0}".format(mei_element.id))
        pass
    
    def _create_scoredef(self, mei_element):
        lg.debug("Creating scoredef: {0}".format(mei_element.id))
        pass
    
    def _create_staffgrp(self, mei_element):
        lg.debug("Creating staffgrp: {0}".format(mei_element.id))
        pass
    
    def _create_staffdef(self, mei_element):
        lg.debug("Creating staffgrp: {0}".format(mei_element.id))
        pass
        
    def _create_layerdef(self, mei_element):
        lg.debug("Creating layerdef: {0}".format(mei_element.id))
        pass
        
    def _create_verse(self, mei_element):
        lg.debug("Creating Verse: {0}".format(mei_element.id))
        
        if mei_element.children:
            for child in mei_element.children:
                if child.name == 'syl':
                    lg.debug("Processing the syllable {0}".format(child.id))
                    lg.debug("Is the child present? {0}".format(child in self.__flat_score))
                    # self.__flat_score.remove(child)



    def _durationConverter(self, d):
        # helper function to deal with the various duration notations.
        # MEI only has integer durations and a restricted set of acceptable
        # text durations.
        if d.isdigit():
            return duration.typeFromNumDict[int(d)]
        elif d in ('maxima', 'long', 'longa', 'breve', 'brevis', 
                    'semibrevis', 'minima', 'semiminima', 'fusa', 'semifusa'):
            return duration.typeToDuration[d]
        else:
            raise TypeError("Invalid duration {0} .".format(d))

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

if __name__ == "__main__":
    from optparse import OptionParser
    p = OptionParser()
    p.add_option("-f", "--file", action="store", help="Mei file to test.")
    (options,args) = p.parse_args()

    c = ConverterMei()
    # cProfile.run('c.parseFile(options.file)')
    c.parseFile(options.file)
    # c._score.show('text')
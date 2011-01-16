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

class MeiConverter(object):
    def __init__(self):
        """docstring for __init__"""
        self._score = stream.Score()
        self._meiDoc = None
        
        self._registry = {}
        
        self._key_sig_registry = {}
        self._key_sig_has_changed = True
        
        self._time_sig_registry = {}
        self._time_sig_has_changed = True
        
        self._clef_registry = {}
        self._clef_has_changed = True
        
        self._mu = None
        self._mc = None
        
        self._objects_to_convert = {
            'note': self._create_note,
            'rest': self._create_rest,
            'slur': self._create_slur,
            'chord': self._create_chord,
            'beam': self._create_beam,
            'mrest': self._create_rest,
            'staffgrp': self._create_staffgrp,
            'staffdef': self._create_staffdef,
            'layerdef': self._create_voice,
            'staff': self._create_staffdef,
            'layer': self._create_voice,
            'measure': self._create_measure,
            'scoredef': self._create_scoredef,
        }
        
        self._contexts = {
            'measure_num': None,
            'staff_num': None,
            'voice_num': None,
            'note': None,
            'chord': None,
            'beam': None
        }
        
    
    def parseFile(self):
        pass
        
    # ====================
    def _create_registries(self):
        self._sections = self._meiDoc.search('section')
        for section in self._sections:
            self._parse_children(section)
    
    def _parse_children(self, element):
        """ This is a recursive function that should breeze through
            all the descendent elements of a given element.
        """
        self.__flattened.append(element)
        if element.name in self._objects_to_convert.keys():
            n = self._objects_to_convert[element.name](element)
            if not isinstance(n, types.NoneType):
                self._registry[element.id] = n
        if element.children:
            map(self._parse_children, element.children)
    
    # =====================
    def _create_staffgrp(self, element):
        lg.debug("Creating staffgrp from {0}".format(element.id))
        # a staff group will just be a spanner element.
        m_staffgrp = spanner.StaffGroup()
        return m_staffgrp

    def _create_measure(self, element):
        # a bit of an anomaly, this one. There is not a direct one-to-one
        # mapping of mei measure to m21 measure. Nevertheless, there are certain
        # tasks that we can condense into the measure creation here.
        lg.debug("Creating a measure, for what it's worth, from {0}".format(element.id))
        
        # get all the staves defined in this measure
        staves = element.children_by_name('staff')
        mid = str(element.attribute_by_name('n').value)
        
        for staff in staves:
            sid = str(staff.attribute_by_name('n').value)
            m_measure = stream.Measure()
            
            address = "{0}.{1}".format(sid,mid)
            self._measure_registry[address] = m_measure
            
            if element.has_attribute('n') and element.measure_number.isdigit():
                m_measure.number = int(element.measure_number)
            
            if element.has_barline:
                lg.debug("Barline is {0} and repeat is {1}".format(element.barline, element.is_repeat))
                if element.is_repeat:
                    m_barline = bar.Repeat()
                    m_barline.style = self._barline_converter(element.barline)
                    if element.barline == "rptstart":
                        m_barline.direction = "start"
                    elif element.barline == "rptend":
                        m_barline.direction = "end"
                    else:
                        raise ConverterMeiError("Could not determine repeat barline type")
                else:
                    m_barline = bar.Barline()
                    m_barline.style = self._barline_converter(element.barline)
                
                m_measure.rightBarline = m_barline
        #return m_measure
        
    def _create_scoredef(self, element):
        # these are global elements. Unless they're changed at a more local
        # (e.g., staffdef or layerdef) level, we'll use these values
        if element.has_attribute('meter.count'):
            self._mc = element.attribute_by_name('meter.count').value
            self._time_sig_has_changed = True
        if element.has_attribute('meter.unit'):
            self._mu = element.attribute_by_name('meter.unit').value
            self._time_sig_has_changed = True
        if element.has_attribute('key.sig'):
            self._ks = element.attribute_by_name('key.sig').value
            self._key_sig_has_changed = True


    def _create_staffdef(self, element):
        staffnum = str(element.attribute_by_name('n').value)
        if staffnum not in self._staff_registry.keys():
            lg.debug("Creating staffdef from {0}".format(element.id))
            self._staff_registry[staffnum] = stream.Part()

        # we put "staff" and "staffdef" construction in the same place,
        # since we want to be able to create a staff on the fly, without a 
        # staffdef. However, many things are only set in the staffdef
        # element. If we don't have a staffdef, we can safely leave at this point.

        if not element.name == "staffdef":
            return
        # clef, key sig, and time sig all have a tuple stored for each staff. 
        # the tuple is (<m21_obj>, bool), where bool is the value of whether or
        # not this object is new and should be put in a measure.
        # clef
        lg.debug("Creating clef.")
        if element.has_attribute('clef.line'):
            cl = int(element.attribute_by_name('clef.line').value)
        else:
            cl = 2 # we'll construct a treble clef by default

        if element.has_attribute('clef.shape'):
            cs = element.attribute_by_name('clef.shape').value
        else:
            cs = "G"

        octavechg = 0
        if element.has_attribute('clef.dis'):
            cd = element.attribute_by_name('clef.dis').value
            if cd == '8':
                octavechg = 1
        if element.has_attribute('clef.dis.place'):
            cdp = element.attribute_by_name('clef.dis.place').value
            if cdp == 'below':
                octavechg = -(octavechg)

        m_clef = clef.standardClefFromXN("{0}{1}".format(cs, cl))

        pdb.set_trace()

        self._clef_registry[staffnum] = [m_clef, True]

        # keysig
        lg.debug("Creating keysig")
        if element.has_attribute('key.sig'):
            ks = element.attribute_by_name('key.sig').value
        else:
            ks = self._ks

        m_ks = key.KeySignature(self._keysig_converter(ks))
        self._key_sig_registry[staffnum] = [m_ks, True]

        # time sig
        lg.debug("Creating timesig")
        m_ts = meter.TimeSignature()
        if element.has_attribute('meter.count'):
            mc = element.attribute_by_name('meter.count').value
        else:
            mc = self._mc

        if element.has_attribute('meter.unit'):
            mu = element.attribute_by_name('meter.unit').value
        else:
            mu = self._mu

        m_ts.load("{0}/{1}".format(mc, mu))
        self._time_sig_registry[staffnum] = [m_ts, True]

    def _create_voice(self, element):
        m_voice = stream.Voice()
        return m_voice

    def _create_note(self, element):
        lg.debug("Creating a note from {0}".format(element.id))
        m_note = note.Note(element.pitch_octave)

        if element.duration:
            normalized_duration = self._duration_converter(element.duration)
            m_note.duration = duration.Duration(normalized_duration)
            if element.is_dotted:
                m_note.duration.dots = int(element.dots)

        if element.tie:
            # there is no such thing as a medial tie in m21 (yet).
            # we'll define the medial as another start.
            tie_translate = {'i': 'start', 'm':'start', 't': 'end'}
            m_note.tie = tie.Tie(tie_translate[element.tie])
            
        if element.articulations:
            # deal with note articulations.
            pass
            
        lg.debug("Returning a note: {0}".format(element.id))

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

    def _create_beam(self, element):
        lg.debug("Creating a beam from {0}".format(element.id))
        m_beam = beam.Beam()

        return m_beam
    # =============================
    # start building the M21 structure
    def _structure_work(self):
        for element in self.__flattened:
            if element.name == "scoredef":
                lg.debug(" ==> Setting a score definition context")

            elif element.name == "measure":
                lg.debug("Setting a measure context.")
                self._contexts['measure_num'] = str(element.attribute_by_name('n').value)
                
            elif element.name == "staff":
                lg.debug(" ==> setting a staff context.")
                self._contexts['staff_num'] = str(element.attribute_by_name('n'),value)
            
            elif element.name == "chord":
                lg.debug(" ==> Setting a chord context")
                
            elif element.name == "beam":
                lg.debug(" ==> Setting a beam context")
                
            elif element.name == "note":
                lg.debug(" ==> Setting a note context ")

            elif element.name == "rest":
                lg.debug(" ==> Setting a rest.")
    
    
    # =============================
    def _keysig_converter(self, mei_ksig):
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

    def _duration_converter(self, d):
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

    def _clef_converter(self, c):
        #c = (shape, line, octavechg)
        # this is stolen from the music21 clef class, for setting the clef
        # from a musicxml attribute list.
        if c == ('G', 1, 0):
            return clef.FrenchViolinClef
        elif c == ('G', 2, 0):
            return clef.TrebleClef
        elif c == ('G', 2, -1):
            return clef.Treble8vbClef
        elif c == ('G', 2, 1):
            return clef.Treble8vaClef
        elif c == ('G', 3, 0):
            return clef.GSopranoClef
        elif c == ('C', 1, 0):
            return clef.SopranoClef
        elif c == ('C', 2, 0):
            return clef.MezzoSopranoClef
        elif c == ('C', 3, 0):
            return clef.AltoClef
        elif c == ('C', 4, 0):
            return clef.TenorClef
        elif c == ('C', 5, 0):
            return clef.CBaritoneClef
        elif c == ('F', 3, 0):
            return clef.FBaritoneClef
        elif c == ('F', 4, 0):
            return clef.BassClef
        elif c == ('F', 4, -1):
            return clef.Bass8vbClef
        elif c == ('F', 4, 1):
            return clef.Bass8vaClef
        elif c == ('F', 5, 0):
            return clef.SubBassClef
        else:
            raise ConverterMeiError('cannot match clef parameters (%s/%s/%s) to a Clef subclass' % (c[0], c[1], c[2]))



if __name__ == "__main__":
    from optparse import OptionParser
    p = OptionParser()
    p.add_option("-f", "--file", action="store", help="Mei file to test.")
    (options,args) = p.parse_args()

    c = MeiConverter()
    # cProfile.run('c.parseFile(options.file)')
    c.parseFile(options.file)
    # c._score.show('text')
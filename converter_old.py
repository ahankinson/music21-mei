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
    #        a. Notes
    #        b. Rests
    #        c. Slurs, Ties, etc.
    #
    
    def __init__(self):
        self._meiDoc = None
        
        self._score = stream.Score()
        
        # registries
        self._structure = {} # {s1: [v1, v2], s2:[v1]}, etc.
        self._measure_registry = {} # {sn-pn-mn: <m21_measure>}
        self._clef_registry = {}
        
        self.__flat_score = None
        self.__processed_elements = {} # {id: <M21 Element>}
        
        self._num_measures = None
        self._num_sections = None
        self._num_voices = None
        self._num_staves = None
        
        self._key_sig = None
        self._key_sig_has_changed = True # set true by default to init the first measure
        
        self._time_sig = None
        self._time_sig_has_changed = True # set true by default to init the first measure
        
        self._clef = None
        self._clef_has_changed = True
        
        
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
        
        # 1. Get staves
        # staves = self._meiDoc.search('staff')
        # for staff in staves:
        #     snum = staff.attribute_by_name('n').value
        #     if snum not in self._staff_rel_voices.keys():
        #         self._staff_rel_voices[snum] = {}
        #     
        # voices = self._meiDoc.search('layer')
        # for voice in voices:
        #     vnum = voice.attribute_by_name('n').value
        #     # which staff does this belong to?
        #     sid = voice.ancestor_by_name('staff').attribute_by_name('n').value
        #     if vnum not in self._staff_rel_voices[sid].keys():
        #         self._staff_rel_voices[sid][vnum] = []
        
        sd = self._meiDoc.search('scoredef')[0]
        mc = sd.attribute_by_name('meter.count').value
        mu = sd.attribute_by_name('meter.unit').value
        ks = sd.attribute_by_name('key.sig').value
        
        self._key_sig = key.KeySignature(self._keysigConverter(ks))
        self._time_sig = meter.TimeSignature()
        self._time_sig.load("{0}/{1}".format(mc, mu))
        
        stfdef = self._meiDoc.search('staffdef')
        for st in stfdef:
            stid = st.attribute_by_name('n').value
            if stid not in self._clef_registry.keys():
                # self._staff_registry[stid] = st
                # self._clef_registry[stid] = self._create_clef(st)
                lg.debug(self._clef_registry)
                
                
        measures = self._meiDoc.search('measure')
        for measure in measures:
            mnum = measure.attribute_by_name('n').value
            staves = measure.descendents_by_name('staff')
            for staff in staves:
                sid = staff.attribute_by_name('n').value
                if sid not in self._structure.keys():                    
                    self._structure[sid] = {}
                voices = staff.descendents_by_name('layer')
                for voice in voices:
                    vid = voice.attribute_by_name('n').value
                    if vid not in self._structure[sid].keys():
                        self._structure[sid][vid] = {}
                    self._structure[sid][vid][mnum] = []
                    
                    # cache the measure object so that we can quickly refer
                    # to it later.
                    self._measure_registry["s{0}-v{1}-m{2}".format(sid, vid, mnum)] = self._create_measure(measure)
                    
                    # finally, we'll gather up all the children on the layer.
                    # note that this does not have to be flattened - we'll deal with nested 
                    # objects later. It just has to be all descendents of that particular
                    # <layer> object.
                    for child in voice.children:
                        self._structure[sid][vid][mnum].append(child)
        
        
        lg.debug(self._structure)
        lg.debug(self._measure_registry)
        lg.debug(self._staff_registry)
        
        for staff in self._structure.keys():
            stg = stream.Part()
            self._score.append(stg)
            
            for voice in self._structure[staff].keys():
                pt = stream.Voice()
                stg.append(pt)
                self._score.append(pt)
                
                for idx, measure in enumerate(sorted(self._structure[staff][voice].keys())):
                    mid = "s{0}-v{1}-m{2}".format(staff, voice, measure)
                    m_measure = self._measure_registry[mid]
                    
                    if idx == 0:
                        # m_measure.clef = self._clef_registry[staff]
                        m_measure.keySignature = self._key_sig
                        m_measure.timeSignature = self._time_sig
                    
                    lg.debug("Working on {0}".format(mid))
                    lg.debug("With the measure: {0}".format(self._measure_registry[mid]))
                    
                    pt.append(self._measure_registry[mid])
                    
                    for el in self._structure[staff][voice][measure]:
                        lg.debug("Element: {0}".format(el))
                        if el.name == "note":
                            self._measure_registry[mid].append(self._create_note(el))
                        elif el.name == "rest":
                            self._measure_registry[mid].append(self._create_rest(el))
                        elif el.name == "beam":
                            for child in el.children:
                                if child.name == "note":
                                    self._measure_registry[mid].append(self._create_note(child))
                                elif child.name == "rest":
                                    self._measure_registry[mid].append(self._create_rest(child))
        
        self._score.show()
        # 
        # score_iter = copy.copy(self.__flat_score)
        # 
        # for idx,el in enumerate(score_iter):
        #     if el.id not in self.__processed_elements.keys():
        #         if el.name in self._registry.keys():
        #             # deal with it
        #             lg.debug("Dealing with: {0}".format(el.name))
        #             m21 = self._trigger_registry(el)
        #             self.__processed_elements[el.id] = m21
        #             
        #             lg.debug("----> Adding {0} to processed elements".format(el.id))
        #     else:
        #         lg.debug("<----- Skipping {0} because it was already processed".format(el))
        #     # else:
        #     #     lg.debug("Removing: {0}".format(el.name))
        #     #     self.__flat_score.remove(el)
        #         
        # 
        # #lg.debug("Leftovers: {0}".format(self.__flat_score))
        # lg.debug("Processed elements: {0}".format(self.__processed_elements))
        
        # get total number of measures:
        
        
        
        
        
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
        
        lg.debug("Returning a note: {0}".format(mei_element.id))
        return m_note
                
        
        
    def _create_measure(self, mei_element):
        m_measure = stream.Measure()
        if mei_element.has_attribute('n') and mei_element.measure_number.isdigit():
            m_measure.number = int(mei_element.measure_number)
        
        if mei_element.has_barline:
            if not mei_element.is_repeat:
                m_barline = bar.Barline()
                m_barline.style = self._barlineConverter(mei_element.barline)
            else:
                m_barline = bar.Repeat()
                m_barline.style = self._barlineConverter(mei_element.barline)
                if mei_element.barline is "rptstart":
                    m_barline.direction = "start"
                elif mei_element.barline is "rptend":
                    m_barline.direction = "end"
            m_measure.rightBarline = m_barline
        
        if self._key_sig_has_changed:
            m_measure.keyIsNew = True
            m_measure.keySignature = self._key_sig
            self._key_sig_has_changed = False
            
        
        if self._time_sig_has_changed:
            m_measure.timeSignatureIsNew = True
            m_measure.timeSignature = self._time_sig
            self._time_sig_has_changed = False
            
        # if self._clef_has_changed:
        #     m_measure.clefIsNew = True
        #     m_measure.clef = self._clef
        #     self._clef_has_changed = False
        
        lg.debug("Returning a measure. {0}".format(mei_element.id))
        return m_measure
    
    def _create_rest(self, mei_element):
        lg.debug("Creating rest: {0}".format(mei_element.id))
        m_rest = note.Rest()
        
        if mei_element.duration:
            normalized_duration = self._durationConverter(mei_element.duration)
            m_rest.duration = duration.Duration(normalized_duration)
            if mei_element.is_dotted:
                m_rest.duration.dots = int(mei_element.dots)
        return m_rest
    
    def _create_chord(self, mei_element):
        lg.debug("Creating chord: {0}".format(mei_element.id))
        pass
    
    def _create_clef(self, mei_element):
        # takes a scoredef element; registers clef information on the converter object
        lg.debug("Creating a clef.")
        
        m_clef = clef.Clef()
        
        cl = int(mei_element.attribute_by_name('clef.line').value)
        cs = mei_element.attribute_by_name('clef.shape').value
        
        m_clef.line = cl
        m_clef.sign = cs
        
        octavechg = 0
        if mei_element.has_attribute('clef.dis'):
            cd = mei_element.attribute_by_name('clef.dis').value
            if cd == '8':
                octavechg = 1
                
        if mei_element.has_attribute('clef.dis.place'):
            cdp = mei_element.attribute_by_name('clef.dis.place').value
            if cdp == 'below':
                octavechg = -(octavechg)
        
        # this should be moved into the music21 clef class. Pretty Please?
        params = (cs, cl, octavechg)
        if params == ('G', 1, 0):
            m_clef.__class__ = clef.FrenchViolinClef
        elif params == ('G', 2, 0):
            m_clef.__class__ = clef.TrebleClef
        elif params == ('G', 2, -1):
            m_clef.__class__ = clef.Treble8vbClef
        elif params == ('G', 2, 1):
            m_clef.__class__ = clef.Treble8vaClef
        elif params == ('G', 3, 0):
            m_clef.__class__ = clef.GSopranoClef
        elif params == ('C', 1, 0):
            m_clef.__class__ = clef.SopranoClef
        elif params == ('C', 2, 0):
            m_clef.__class__ = clef.MezzoSopranoClef
        elif params == ('C', 3, 0):
            m_clef.__class__ = clef.AltoClef
        elif params == ('C', 4, 0):
            m_clef.__class__ = clef.TenorClef
        elif params == ('C', 5, 0):
            m_clef.__class__ = clef.CBaritoneClef
        elif params == ('F', 3, 0):
            m_clef.__class__ = clef.FBaritoneClef
        elif params == ('F', 4, 0):
            m_clef.__class__ = clef.BassClef
        elif params == ('F', 4, -1):
            m_clef.__class__ = clef.Bass8vbClef
        elif params == ('F', 4, 1):
            m_clef.__class__ = clef.Bass8vaClef
        elif params == ('F', 5, 0):
            m_clef.__class__ = clef.SubBassClef
        else:
            raise clef.ClefException('cannot match clef parameters (%s/%s/%s) to a Clef subclass' % (params[0], params[1], params[2]))
        
        lg.debug(m_clef)
        
        return m_clef
        
    
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
                    self.__processed_elements.append(child)
        self.__processed_elements.append(mei_element)


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
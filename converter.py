from pymei.Import import convert as mei_convert
# from pymei.Helpers import flatten
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
import copy
lg = logging.getLogger('pymei')

class MeiConverterError(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return repr(self.message)


class MeiConverter(object):
    def __init__(self):
        self.__flatten = []
        self._mei_doc = None
        self._score = stream.Score()
        
        
        self._staff_registry = []
        self._section_registry = []
        self._measure_registry = []
        self._voice_registry = []
        self._chord_registry = []
        self._nr_registry = [] # note and rest registry
        
        # these are per-staff (staffdef) registries
        self._clef_registry = []
        self._key_sig_registry = []
        self._time_sig_registry = []
        
        # these are global (scoredef) registries
        self._global_clef = None
        self._global_key_sig = None
        self._global_time_sig = None
        
        self._mc = None # global meter count
        self._mu = None # global meter unit
        self._ks = None # global key signature
        self._cl = None # global clef line
        self._cs = None # global clef shape
        
        self._contexts = {
            'section_num': None,
            'measure_num': None,
            'staff_num': None,
            'voice_num': None,
            'measure': None,
            'clef': {},  # contexts['clef']['<staff_num>']
            'key_sig': {},
            'chord': None
        }
        
        
    def parseFile(self, filename):
        self._mei_doc = mei_convert(filename)
        self._flatten_structure(self._mei_doc.gettoplevel())
        self._create_registries()
        self._parse_structure()
        
        
        # lg.debug(sorted(self._section_registry.values()))
        # lg.debug(self._measure_registry)
        # lg.debug(self._staff_registry)
        # lg.debug(self._contexts)
        
        # for k,v in self._voice_registry.iteritems():
        #     section,staff,measure,voice = k.split(".")
        #     if section == "0":
        #         measure_address = 
        #         self._measure_registry[""]
        
        for k,v in self._staff_registry:
            if k.startswith("0"):
                self._score.insert(0, v)
        
        self._score.show('text')
        
    # ==================
    def _flatten_structure(self, element):
        self.__flatten.append(element)
        if element.children:
            map(self._flatten_structure, element.children)
    
    def _create_registries(self):
        sections = self._mei_doc.search('section')
        
        # set a number for each section. This isn't usually set.
        for snum, section in enumerate(sections):
            # unlike others, this registry stores the MEI section object as key, and the number as
            # the value. This is so we can set context later...
            self._section_registry.append((section, str(snum)))
            
            # we need a list of unique measure and staff "n" values. This is 
            # a really simple way of getting them...
            staves = section.descendants_by_name('staff')
            sids = set([str(s.attribute_by_name('n').value) for s in staves])
            
            measures = section.descendants_by_name('measure')
            mids = set([str(m.attribute_by_name('n').value) for m in measures])
            
            for measure in measures:
                mnum = str(measure.attribute_by_name('n').value)
                
                staves = measure.descendants_by_name('staff')
                for staff in staves:
                    stnum = str(staff.attribute_by_name('n').value)
                    staff_address = "{0}.{1}".format(snum, stnum)
                    if staff_address not in dict(self._staff_registry).keys():
                        s = stream.Part()
                        self._staff_registry.append((staff_address, s))
                    else:
                        s = dict(self._staff_registry)[staff_address]
                    # construct the measures here.
                    measure_address = "{0}.{1}.{2}".format(snum, stnum, mnum)
                    if measure_address not in dict(self._measure_registry)  .keys():
                        m = self._create_measure(measure)
                        self._measure_registry.append((measure_address, m))
                    else:
                        m = dict(self._measure_registry)[measure_address]
                    # s.append(m)
                    
                    voices = staff.descendants_by_name('layer')
                    for voice in voices:
                        vnum = str(voice.attribute_by_name('n').value)
                        voice_address = "{0}.{1}.{2}.{3}".format(snum, stnum, mnum, vnum)
                        if voice_address not in dict(self._voice_registry).keys():
                            v = stream.Voice()
                            self._voice_registry.append((voice_address, v))
                        else:
                            v = dict(self._voice_registry)[voice_address]
                        # m.append(v)

    
    # ==================
    def _parse_structure(self):
        for element in self.__flatten:
            if element.name == "section":
                snum = dict(self._section_registry)[element] # this should *always* be filled.
                self._contexts['section_num'] = snum
            elif element.name == "scoredef":
                self._create_scoredef(element)
                
                
                
            elif element.name == "staffdef":
                self._create_staffdef(element)
            elif element.name == "measure":
                self._contexts['measure_num'] = str(element.attribute_by_name('n').value)             
            elif element.name == "staff":
                self._contexts['staff_num'] = str(element.attribute_by_name('n').value)
                # set both the staff and measure contexts here because we 
                # have all the information we need now.
                staff_address = "{0}.{1}".format(self._contexts['section_num'], self._contexts['staff_num'])
                lg.debug("Staff Address: {0}".format(staff_address))
                self._contexts['staff'] = dict(self._staff_registry)[staff_address]
                
                clf = self._contexts['clef'][self._contexts['staff_num']]
                keysig = self._contexts['key_sig'][self._contexts['staff_num']]
                # try:
                #     clf = dict(self._clef_registry)[staff_address]
                #     self._contexts['clef'][self._contexts['staff_num']] = clf
                # except KeyError:
                #     # we have no clef for this staff, so we'll take it from the global registry.\
                #     lg.debug("No Clef!")
                #     clf = self._contexts['clef'][self._contexts['staff_num']]
                #     # self._contexts['clef'] = clf
                
                
                # try:
                #     keysig = dict(self._key_sig_registry)[staff_address]
                #     self._contexts['key_signature'] = keysig
                # except KeyError:
                #     keysig = self._global_keysig
                #     self._contexts['key_signature'] = keysig
                
                try:
                    timesig = dict(self._time_sig_registry)[staff_address]
                    self._contexts['time_signature'] = timesig
                except KeyError:
                    timesig = self._global_timesig
                    self._contexts['time_signature'] = timesig
                
                
                measure_address = "{0}.{1}.{2}".format(self._contexts['section_num'], self._contexts['staff_num'], self._contexts['measure_num'])
                m = dict(self._measure_registry)[measure_address]
                
                lg.debug("Clef: {0}".format(clf))
                
                m.clef = clf[0]
                m.clefIsNew = True
                # if clf[1] is True:
                #     clf[1] = False
                #     m.clef = clf[0]
                #     m.clefIsNew = True
                # else:
                #     m.clefIsNew = False
                
                
                m.keySignature = keysig[0]
                m.keyIsNew = True
                
                # if keysig[1] is True:
                #     keysig[1] = False
                #     m.keySignature = keysig[0]
                #     m.keyIsNew = True
                # else:
                #     m.keyIsNew = False
                
                m.timeSignature = timesig[0]
                m.timeSignatureIsNew = True
                # if timesig[1] is True:
                #     timesig[1] = False
                #     m.timeSignature = timesig[0]
                #     m.timeSignatureIsNew = True
                # else:
                #     m.timeSignatureIsNew = False
                    
                self._contexts['measure'] = m
                self._contexts['staff'].insert(0, self._contexts['measure'])
                
            elif element.name == "layer":
                self._contexts['voice_num'] = str(element.attribute_by_name('n').value)
                voice_address = "{0}.{1}.{2}.{3}".format(self._contexts['section_num'], self._contexts['staff_num'], self._contexts['measure_num'], self._contexts['voice_num'])
                self._contexts['voice'] = dict(self._voice_registry)[voice_address]
                self._contexts['measure'].append(self._contexts['voice'])
            elif element.name == "chord":
                # create chord
                c = self._create_chord(element)
                self._chord_registry.append((element.id, c))
                self._contexts['voice'].append(c)
            elif element.name == "note":
                # create note context
                # check if in chord
                    # add to chord and continue
                # check if in beam
                    # add to beam and continue
                n = self._create_note(element)
                self._nr_registry.append((element.id, n))
                
                
                if element.ancestor_by_name('chord'):
                    # set the chord context and add the note.
                    # since a chord only needs a pitch name, we don't have 
                    # to set the whole note, just the pitch.
                    c_id = element.ancestor_by_name('chord').id
                    m_chord = dict(self._chord_registry)[c_id]
                    m_chord.pitches.append(n.pitch)
                else:
                    # add the note directly to the voice
                    self._contexts['voice'].append(n)
                    
            elif element.name == "rest":
                # create a rest context
                # check if in chord
                    # add to chord and continue
                # check if in beam
                    # add to beam and continue
                # if neither, add to voice context
                    # and continue
                r = self._create_rest(element)
                self._contexts['voice'].append(r)
                self._nr_registry.append((element.id, r))
                
            elif element.name == "mrest":
                # create a full measure rest
                d = self._contexts['measure'].duration
                r = self._create_mrest(element)
                r.duration = d
                self._contexts['voice'].append(r)
                self._nr_registry.append((element.id, r))
            
            elif element.name == "clefchange":
                clf = self._create_clefchange(element)
                staff_address = "{0}.{1}".format(self._contexts['section_num'], self._contexts['staff_num'])
                measure_address = "{0}.{1}.{2}".format(self._contexts['section_num'], self._contexts['staff_num'], self._contexts['measure_num'])
                m = dict(self._measure_registry)[measure_address]
                
                m.clef = clf
                m.clefIsNew = True
                self._contexts['clef'][self._contexts['staff_num']] = [clf, True]
                
                
                
                
        
        # second pass - this deals with spanning elements - slurs, tuplets, etc.
        lg.debug(" ======== Second Pass ========")
        for element in self.__flatten:
            if element.name == "tupletspan":
                self._create_tupletspan(element)
            elif element.name == "slur":
                pass
            
        
    # ===================
    def _create_note(self, element):
        # lg.debug("Creating a note from {0}".format(element.id))
        pname = element.pitchname
        accid = self._accidental_converter(element.accidentals)
        octav = element.octave
        nt = "".join([pname, accid, octav])
        
        m_note = note.Note(nt)
        
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

        return m_note    
        
    def _create_rest(self, element):
        # lg.debug("Creating rest: {0}".format(element.id))
        m_rest = note.Rest()

        if element.duration:
            normalized_duration = self._duration_converter(element.duration)
            m_rest.duration = duration.Duration(normalized_duration)
            if element.is_dotted:
                m_rest.duration.dots = int(element.dots)
        return m_rest
        
    def _create_mrest(self, element):
        # lg.debug("Creating rest: {0}".format(element.id))
        m_mrest = note.Rest()
        return m_mrest

    def _create_measure(self, element):
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
                if element.barline == "rptstart":
                    m_barline.direction = "start"
                elif element.barline == "rptend":
                    m_barline.direction = "end"
            m_measure.rightBarline = m_barline
        
        return m_measure

    def _create_scoredef(self, element):
        if element.has_attribute('clef.line') or element.has_attribute('clef.shape'):
            m_clef = self._create_clef(element)
            self._global_clef = [m_clef, True]
        
        if element.has_attribute('meter.count'):
            m_ts = self._create_timesig(element)
            self._global_timesig = [m_ts, True]
        
        if element.has_attribute('key.sig'):
            m_ks = self._create_keysig(element)
            self._global_keysig = [m_ks, True]
    
    def _create_staffdef(self, element):
        staffnum = element.attribute_by_name('n').value
        section = element.ancestor_by_name('section')
        
        if isinstance(section, types.NoneType):
            # we have a header staffdef. Assume the beginning of the file
            sectionnum = "0"
        else:
            sectionnum = dict(self._section_registry)[section]
        staff_address = "{0}.{1}".format(sectionnum, staffnum)
        
        
        # if staffnum not in self._staff_registry.keys():
        #     lg.debug("Creating staffdef from {0}".format(element.id))
        #     self._staff_registry[staffnum] = stream.Part()

        # clef, key sig, and time sig all have a tuple stored for each staff. 
        # the tuple is (<m21_obj>, bool), where bool is the value of whether or
        # not this object is new and should be put in a measure.
        # clef
        lg.debug("Creating clef.")
        m_clef = self._create_clef(element)
        self._contexts['clef'][staffnum] = [m_clef, True]
        # self._global_clef = [m_clef, True]
        # self._clef_registry.append((staff_address, [m_clef, True]))

        # keysig
        lg.debug("Creating keysig")
        m_ks = self._create_keysig(element)
        self._contexts['key_sig'][staffnum] = [m_ks, True]
        # self._global_keysig = [m_ks, True]
        # self._key_sig_registry.append((staff_address, [m_ks, True]))

        # time sig
        lg.debug("Creating timesig")
        m_ts = self._create_timesig(element)
        self._global_timesig = [m_ts, True]
        self._time_sig_registry.append((staff_address, [m_ts, True]))

    def _create_clef(self, element):
        if element.has_attribute('clef.line'):
            cl = int(element.attribute_by_name('clef.line').value)
            self._cl = cl
        else:
            cl = self._cl

        if element.has_attribute('clef.shape'):
            cs = element.attribute_by_name('clef.shape').value
            self._cs = cs
        else:
            cs = self._cs
        
        octavechg = 0
        if element.has_attribute('clef.dis'):
            cd = element.attribute_by_name('clef.dis').value
            if cd == '8':
                octavechg = 1
        if element.has_attribute('clef.dis.place'):
            cdp = element.attribute_by_name('clef.dis.place').value
            if cdp == 'below':
                octavechg = -(octavechg)
                
        # lg.debug(element)
        # lg.debug("{0} and {1}".format(cs, cl))
        return clef.standardClefFromXN("{0}{1}".format(cs, cl))
    
    def _create_keysig(self, element):
        if element.has_attribute('key.sig'):
            ks = element.attribute_by_name('key.sig').value
            self._ks = ks
        else:
            ks = self._ks
        return key.KeySignature(self._keysig_converter(ks))
    
    def _create_timesig(self, element):
        m_ts = meter.TimeSignature()
        if element.has_attribute('meter.count'):
            mc = element.attribute_by_name('meter.count').value
            self._mc = mc
        else:
            mc = self._mc
            
        if element.has_attribute('meter.unit'):
            mu = element.attribute_by_name('meter.unit').value
            self._mu = mu
        else:
            mu = self._mu
        
        m_ts.load("{0}/{1}".format(mc, mu))
        return m_ts
    
    def _create_chord(self, element):
        m_chord = chord.Chord()
        if element.has_attribute('dur'):
            normalized_duration = self._duration_converter(element.duration)
            m_chord.duration = duration.Duration(normalized_duration)
            if element.is_dotted:
                m_chord.duration.dots = int(element.dots)
        return m_chord
    
    def _create_clefchange(self, element):
        if element.has_attribute('shape'):
            cs = element.attribute_by_name('shape').value
        else:
            cs = self._cs
        
        if element.has_attribute('line'):
            cl = int(element.attribute_by_name('line').value)
        else:
            cl = self._cl
        
        octavechg = 0
        if element.has_attribute('dis'):
            cd = element.attribute_by_name('dis').value
            if cd == '8':
                octavechg == 1
        if element.has_attribute('dis.place'):
            cdp = element.attribute_by_name('dis.place').value
            if cdp == 'below':
                octavechg = -(octavechg)
        return clef.standardClefFromXN("{0}{1}".format(cs, cl))
        
    
    # these are second-pass creation functions. It's safe to assume our registries
    # are fully populated by now.    
    def _create_tupletspan(self, element):
        if element.has_attribute('startid'):
            startid = element.attribute_by_name('startid').value
        if element.has_attribute('endid'):
            endid = element.attribute_by_name('endid').value
        
        tupletmembers = self._get_range(['note', 'rest'], startid, endid)
        
        if element.has_attribute('num'):
            num = int(element.attribute_by_name('num').value)
        if element.has_attribute('numbase'):
            numbase = int(element.attribute_by_name('numbase').value)
        
        for member in tupletmembers:
            # either a note or a rest for now.
            m_nr = dict(self._nr_registry)[member.id]
            m_nr.duration.appendTuplet(duration.Tuplet(num, numbase, m_nr.duration.type))
            
            
        
    # =============================
    def _keysig_converter(self, mei_ksig):
        """ 
            Converts a MEI key signature (e.g. 4f, 5s) to absolute circle-of-fifths 
            representation (-/+, e.g. -1 = 1f; +1 = 1s; 4f = -4; 5s = +5)
        """
        if not mei_ksig[0].isdigit():
            raise MeiConverterError("Only key signatures with the form <num><str> are supported, e.g. 0, 4f, 5s.")

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
            raise MeiConverterError("Could not convert barline.")
    
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
            raise MeiConverterError('cannot match clef parameters (%s/%s/%s) to a Clef subclass' % (c[0], c[1], c[2]))
    
    def _get_range(self, names, startid, endid):
        """ Gets all objects of <names> between <startid> and <endid>
            
            For example, if we have a tuplet span of 3 notes with a startid of 1
            and an end id of 3, calling:
            
            n = _get_range(['note', 'rest', 'chord'], '1', '3')
            
            will return a list of all MEI note, rest, and chord objects between 1 and 3, regardless
            of their nested position.        
        """
        if not hasattr(names, "__iter__"):
            raise MeiConverterError("You must supply an iterable of names for the name element")
        
        start = [el for el in self.__flatten if el.id == startid]
        end = [el for el in self.__flatten if el.id == endid]
        
        if not start and end:
            raise MeiConverterError("One element was found (start or end), but not the other. Cannot continue.")
            
        startidx = self.__flatten.index(start[0])
        endidx = self.__flatten.index(end[0]) + 1 # we want to include the end element, so slice one up from the end id.
        sublist = self.__flatten[startidx:endidx]
        elrange = [el for el in sublist if el.name in names]
        return elrange
    
    def _accidental_converter(self, accid):
        """ Takes an MEI accidental and returns the appropriate M21 conversion."""
        conv = {
            'n': 'n',
            's': '#', 
            'f': '-', 
            'ss': '##', 
            'x': '##', 
            'ff': '--',
            'xs': '###',
            'tb': '---'
        }
        try:
            return conv[accid]
        except KeyError:
            return ''
        
        
        
    
if __name__ == "__main__":
    from optparse import OptionParser
    p = OptionParser()
    p.add_option("-f", "--file", action="store", help="Mei file to test.")
    (options,args) = p.parse_args()

    conv = MeiConverter()
    # cProfile.run('c.parseFile(options.file)')
    conv.parseFile(options.file)
    # c._score.show('text')
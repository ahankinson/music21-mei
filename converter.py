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

import pdb

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
        
        # self._staff_registry = []
        # self._section_registry = []
        # self._measure_registry = []
        # self._voice_registry = []
        # self._chord_registry = []
        # self._nr_registry = [] # note and rest registry
        
        # these are global (scoredef) registries
        # self._global_clef = None
        # self._global_key_sig = None
        # self._global_time_sig = None
        
        self._mc = None # global meter count
        self._mu = None # global meter unit
        self._ks = None # global key signature
        self._cl = None # global clef line
        self._cs = None # global clef shape
        
        self._contexts = {
            'sections': {},
            'section_num': None,
            'measures': {},
            'measure_num': None,
            'staves': {},
            'staff_num': None,
            'voices': {},
            'voice_num': None,
            'section': None,
            'measure': None,
            'staff': None,
            'voice': None,
            'clef': {},  # contexts['clef']['<staff_num>']
            'key_sig': {},
            'time_sig': {},
            'chords': {},
            'chord': None,
            'note_rest': {}
        }
        
        
    def parseFile(self, filename):
        self._mei_doc = mei_convert(filename)
        self._flatten_structure(self._mei_doc.gettoplevel())
        self._create_registries()
        self._parse_structure()
        
        # pdb.set_trace()
        
        for k,v in sorted(self._contexts['staves'].iteritems()):
            lg.debug("Inserting {0}".format(k))
            self._score.insert(0, v)
        
        pdb.set_trace()
        
        lg.debug("Done constructing. Showing now.")
        self._score.show('text')
        pdb.set_trace()
        
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
            self._contexts['sections'][section] = str(snum)
            # self._section_registry.append((section, str(snum)))
            measures = section.descendants_by_name('measure')
            
            for measure in measures:
                mnum = str(measure.attribute_by_name('n').value)
                
                staves = measure.descendants_by_name('staff')
                for staff in staves:
                    stnum = str(staff.attribute_by_name('n').value)
                    # staff_address = "{0}.{1}".format(snum, stnum)
                    # if staff_address not in dict(self._staff_registry).keys():
                    if stnum not in self._contexts['staves'].keys():
                        s = stream.Part()
                        self._contexts['staves'][stnum] = s
                        self._contexts['measures'][stnum] = {}
                        self._contexts['voices'][stnum] = {}
                    else:
                        s = self._contexts['staves'][stnum]
                    # construct the measures here.
                    # measure_address = "{0}.{1}.{2}".format(snum, stnum, mnum)
                    # if measure_address not in dict(self._measure_registry).keys():
                    if mnum not in self._contexts['measures'][stnum].keys():
                        m = self._create_measure(measure)
                        self._contexts['measures'][stnum][mnum] = m
                        self._contexts['voices'][stnum][mnum] = {}
                    else:
                        m = self._contexts['measures'][stnum][mnum]
                    # s.append(m)
                    
                    voices = staff.descendants_by_name('layer')
                    for voice in voices:
                        vnum = str(voice.attribute_by_name('n').value)
                        # voice_address = "{0}.{1}.{2}.{3}".format(snum, stnum, mnum, vnum)
                        # if voice_address not in dict(self._voice_registry).keys():
                        if vnum not in self._contexts['voices'][stnum][mnum].keys():
                            v = stream.Voice()
                            self._contexts['voices'][stnum][mnum][vnum] = v
                        else:
                            v = self._contexts['voices'][stnum][mnum][vnum]
                        # m.append(v)

    
    # ==================
    def _parse_structure(self):
        for element in self.__flatten:
            if element.name == "section":
                snum = self._contexts['sections'][element] # this should *always* be filled.
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
                # staff_address = "{0}.{1}".format(self._contexts['section_num'], self._contexts['staff_num'])
                self._contexts['staff'] = self._contexts['staves'][self._contexts['staff_num']]
                
                try:
                    clf = self._contexts['clef'][self._contexts['staff_num']]
                except KeyError:
                    clf = self._contexts['clef']['global']
                
                try:
                    keysig = self._contexts['key_sig'][self._contexts['staff_num']]
                except KeyError:
                    keysig = self._contexts['key_sig']['global']
                
                try:
                    timesig = self._contexts['time_sig'][self._contexts['staff_num']]
                except KeyError:
                    timesig = self._contexts['time_sig']['global']
                
                m = self._contexts['measures'][self._contexts['staff_num']][self._contexts['measure_num']]
                
                if clf[1] is True:
                    m.clef = clf[0]
                    m.clefIsNew = True
                    clf[1] = False
                else:
                    m.clefIsNew = False
                    
                if keysig[1] is True:
                    m.keySignature = keysig[0]
                    m.keyIsNew = True
                    keysig[1] = False
                else:
                    m.keyIsNew = False
                
                if timesig[1] is True:
                    m.timeSignature = timesig[0]
                    m.timeSignatureIsNew = True
                    timesig[1] = False
                else:
                    m.timeSignatureIsNew = False
                
                self._contexts['staff'].insert(0, self._contexts['measures'][self._contexts['staff_num']][self._contexts['measure_num']])
                
            elif element.name == "layer":
                self._contexts['voice_num'] = str(element.attribute_by_name('n').value)
                voice_address = "{0}.{1}.{2}.{3}".format(self._contexts['section_num'], self._contexts['staff_num'], self._contexts['measure_num'], self._contexts['voice_num'])
                self._contexts['voice'] = self._contexts['voices'][self._contexts['staff_num']][self._contexts['measure_num']][self._contexts['voice_num']]
                
                # since each voice is a concurrent stream of notes, we insert them at index 0 in the measure.
                self._contexts['measures'][self._contexts['staff_num']][self._contexts['measure_num']].insert(0, self._contexts['voice'])

            elif element.name == "chord":
                # create chord
                c = self._create_chord(element)
                self._contexts['chords'][element.id] = c
                self._contexts['voice'].append(c)
                
                lg.debug("Checking for beams...")
                if element.has_ancestor('beam'):
                    lg.debug("Yup! Beams!")
                    lg.debug("Beam found for element {0} and duration {1}".format(element.id, c.duration.type))
                    if c.duration.type == "eighth":
                        c.beams.fill("eighth")
                    elif c.duration.type == "16th":
                        c.beams.fill("16th")
                    elif c.duration.type == "32nd":
                        c.beams.fill("32nd")
                    elif c.duration.type == "64th":
                        c.beams.fill("64th")
                    elif c.duration.type == "128th":
                        c.beams.fill("128th")
                    elif c.duration.type == "256th":
                        c.beams.fill("256th")
                    else:
                        pass
                    
                    first_beam = element.ancestor_by_name('beam').first_child
                    last_beam = element.ancestor_by_name('beam').last_child
                    
                    lg.debug("{0}".format(element.ancestor_by_name('beam')))
                    if element == first_beam:
                        lg.debug("Element is first")
                        c.beams.setAll('start')
                    if element == last_beam:
                        lg.debug("Element is last")
                        c.beams.setAll('stop')
                    
                    if element != first_beam and element != last_beam:
                        lg.debug("Element continues a beam.")
                        c.beams.setAll('continue')
                    
                    
                    if None in c.beams.beamsList:
                        pdb.set_trace()
                    
                
            elif element.name == "beam":
                # create beam
                # set beam context
                pass
            
	    elif element.name == "note":
                # create note context
                # check if in chord
                    # add to chord and continue
                # check if in beam
                    # add to beam and continue
                n = self._create_note(element)
                self._contexts['note_rest'][element.id] = n
                
                if element.has_attribute('stem.dir'):
                    lg.debug("Setting stem direction.")
                    n.stemDirection = element.attribute_by_name('stem.dir')
                
                if element.ancestor_by_name('chord'):
                    # set the chord context and add the note.
                    # since a chord only needs a pitch name, we don't have 
                    # to set the whole note, just the pitch.
                    c_id = element.ancestor_by_name('chord').id
                    m_chord = self._contexts['chords'][c_id]
                    m_chord.pitches.append(n.pitch)
                else:
                    # add the note directly to the voice
                    self._contexts['voice'].append(n)
                
                lg.debug("Checking for beams...")
                if element.has_ancestor('beam'):
                    lg.debug("Yup! Beams!")
                    if n.duration.type == "eighth":
                        n.beams.fill("eighth")
                    elif n.duration.type == "16th":
                        n.beams.fill("16th")
                    elif n.duration.type == "32nd":
                        n.beams.fill("32nd")
                    elif n.duration.type == "64th":
                        n.beams.fill("64th")
                    elif n.duration.type == "128th":
                        n.beams.fill("128th")
                    elif n.duration.type == "256th":
                        n.beams.fill("256th")
                    else:
                        pass

                    first_beam = element.ancestor_by_name('beam').first_child
                    last_beam = element.ancestor_by_name('beam').last_child

                    lg.debug("{0}".format(element.ancestor_by_name('beam')))
                    if element == first_beam:
                        lg.debug("Element is first")
                        n.beams.setAll('start')
                    if element == last_beam:
                        lg.debug("Element is last")
                        n.beams.setAll('stop')

                    if element != first_beam and element != last_beam:
                        lg.debug("Element continues a beam.")
                        n.beams.setAll('continue')


                    if None in n.beams.beamsList:
                        pdb.set_trace()
                    
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
                self._contexts['note_rest'][element.id] = r
                
            elif element.name == "mrest":
                # create a full measure rest
                try:
                    d = self._contexts['time_sig'][self._contexts['staff_num']][0].barDuration
                except KeyError:
                    d = self._contexts['time_sig']['global'][0].barDuration
                    
                r = self._create_mrest(element)
                r.duration = d
                self._contexts['voices'][self._contexts['staff_num']][self._contexts['measure_num']][self._contexts['voice_num']].append(r)
                self._contexts['note_rest'][element.id] = r
            
            elif element.name == "clefchange":
                clf = self._create_clefchange(element)
                m = self._contexts['measures'][self._contexts['staff_num']][self._contexts['measure_num']]
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
        
        lg.debug(" ======== Third Pass =========")
        for sect,snum in self._contexts['sections'].iteritems():
            lg.debug("Section Number: {0}".format(snum))
            sorted_staff = sorted(self._contexts['staves'], key=int)
            for stnum in sorted_staff:
                staff = self._contexts['staves'][stnum]
                lg.debug("Staff Number: {0}".format(stnum))
                
                oset = 0
                vdur = 0
                sorted_meas = sorted(self._contexts['measures'][stnum], key=int)
                for mnum in sorted_meas:
                    meas = self._contexts['measures'][stnum][mnum]
                    lg.debug("Measure Number: {0}".format(meas.number))
                    # meas.makeBeams()
                    meas.makeAccidentals()
                    for vnum, voic in sorted(self._contexts['voices'][stnum][mnum].iteritems()):
                        voic.makeTupletBrackets()
                        # get the longest voice duration in the measure.
                        if voic.duration.quarterLength > vdur:
                            vdur = voic.duration.quarterLength
                    
                    if oset == 0:
                        meas.offset = oset
                        oset = 1
                        lg.debug('oset is now: {0}'.format(oset))
                    else:
                        meas.offset = oset
                        oset = oset + vdur
                        lg.debug('oset is now: {0}'.format(oset))
                    
                    
    # ===================
    def _create_note(self, element):
        # lg.debug("Creating a note from {0}".format(element.id))
        pname = element.pitchname
        accid = self._accidental_converter(element.accidentals)
        octav = element.octave
        nt = "".join([pname, accid, octav])
        
        m_note = note.Note(nt)
        
        if element.duration:
            # the note itself has the duration
            normalized_duration = self._duration_converter(element.duration)
            m_note.duration = duration.Duration(normalized_duration)
            if element.is_dotted:
                m_note.duration.dots = int(element.dots)
        elif element.has_ancestor('chord'):
            anc = element.ancestor_by_name('chord')
            normalized_duration = self._duration_converter(anc.duration)
            m_note.duration = duration.Duration(normalized_duration)
        
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
            self._contexts['clef']['global'] = [m_clef, True]
            # self._global_clef = [m_clef, True]
        
        if element.has_attribute('meter.count'):
            m_ts = self._create_timesig(element)
            self._contexts['time_sig']['global'] = [m_ts, True]
            # self._global_timesig = [m_ts, True]
        
        if element.has_attribute('key.sig'):
            m_ks = self._create_keysig(element)
            self._contexts['key_sig']['global'] = [m_ks, True]
            # force all staves to reset their key signatures.
            for k,v in self._contexts['key_sig'].iteritems():
                self._contexts['key_sig'][k] = [m_ks, True]
    
    def _create_staffdef(self, element):
        staffnum = element.attribute_by_name('n').value
        section = element.ancestor_by_name('section')
        
        if isinstance(section, types.NoneType):
            # we have a header staffdef. Assume the beginning of the file
            sectionnum = "0"
        else:
            sectionnum = self._contexts['section'][section]
        staff_address = "{0}.{1}".format(sectionnum, staffnum)
        
        
        # if staffnum not in self._staff_registry.keys():
        #     lg.debug("Creating staffdef from {0}".format(element.id))
        #     self._staff_registry[staffnum] = stream.Part()

        # clef, key sig, and time sig all have a tuple stored for each staff. 
        # the tuple is (<m21_obj>, bool), where bool is the value of whether or
        # not this object is new and should be put in a measure.
        # clef
        lg.debug("Creating clef.")
        if element.has_attribute('clef.line') and element.has_attribute('clef.shape'):
            m_clef = self._create_clef(element)
            self._contexts['clef'][staffnum] = [m_clef, True]

        # keysig
        lg.debug("Creating keysig")
        if element.has_attribute('key.sig'):
            m_ks = self._create_keysig(element)
            self._contexts['key_sig'][staffnum] = [m_ks, True]

        # time sig
        if element.has_attribute('meter.count') and element.has_attribute('meter.unit'):
            lg.debug("Creating timesig")
            m_ts = self._create_timesig(element)
            self._contexts['time_sig'][staffnum] = [m_ts, True]

    def _create_clef(self, element):
        cl = int(element.attribute_by_name('clef.line').value)
        cs = element.attribute_by_name('clef.shape').value
        
        octavechg = 0
        if element.has_attribute('clef.dis'):
            cd = element.attribute_by_name('clef.dis').value
            if cd == '8':
                octavechg = 1
        if element.has_attribute('clef.dis.place'):
            cdp = element.attribute_by_name('clef.dis.place').value
            if cdp == 'below':
                octavechg = -(octavechg)
                
        return clef.standardClefFromXN("{0}{1}".format(cs, cl))
    
    def _create_keysig(self, element):
        ks = element.attribute_by_name('key.sig').value
        return key.KeySignature(self._keysig_converter(ks))
    
    def _create_timesig(self, element):
        m_ts = meter.TimeSignature()
        mc = element.attribute_by_name('meter.count').value
        mu = element.attribute_by_name('meter.unit').value
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

        if element.has_attribute('line'):
            cl = int(element.attribute_by_name('line').value)
        
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
            m_nr = self._contexts['note_rest'][member.id]
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
        accid = "".join(accid)
        conv = {
            '': '',
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

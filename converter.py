""" Designed to be plugged into the Music21 converter system. """
from pymei.Import import convert
from pymei.Helpers import flatten
from music21 import stream
from music21 import bar
from music21 import meter
from music21 import key


from music21.mei import translate

import logging
import pprint
lg = logging.getLogger('pymei')
"""
    Score -> stream.Score():
        Staves -> stream.Staff():
            Parts -> stream.Part():
                Measures -> stream.Measure():
                    Notes -> note.Note()
                    Rests -> note.Rest()
                    Dynamics -> dynamics.Dynamic()

"""


# class Staff(stream.Stream):
#     """ This is going to be implemented in m21. We'll just put it here for  
#         now.
#     """
#     pass



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
        self._currentKeySig = None # key sigs can change. This is the current one.
        self._staves = {} # {staffnum: <m21 staff object>}
        
        self.__flat_score = None # the flattened objects in the score.
        
    
    def parseFile(self, fn):
        self._meiDoc = convert(fn)
        self._firstPass()
        self._secondPass()
        
        self._score.append(self._staves.values())
        
        self._score.show('text')
        pass
    
    def _firstPass(self):
        """ 
            Work out what the sections and global values are we need, and 
            set us up the score.
        """
        
        self.__flat_score = flatten(self._meiDoc.search('score')[0])
        score_elements = (
            'scoredef',
            'staffdef'
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
        )
        
        # we don't need to encode sections, but having them sorted here makes it pretty
        # handy to work with them.
        # for section in sections:
        #     se = filter(lambda s: s.name in section_elements, flatten(section))
        #     self._sections[section] = se
        # lg.debug("Section elements: {0}".format(pprint.pprint(self._sections)))
        
        # 
        # lg.debug("Staves: {0}".format(self._staves))
        
    def _secondPass(self):
        # now we build the score.
        # Tonight, we dance!
        
        # staves = filter(lambda s: s.getname() == "staff", self.__flat_score)
        # for staff in staves:
        #     snum = staff.attribute_by_name('n').value
        #     if snum not in self._staves.keys():
        #         st = stream.Staff()
        #         sd = filter(lambda s: s.getname() == 'staffdef' and s.attribute_by_name('n').value == snum, 
        #                         self._score_defs)[0]
        #         
        #         label = sd.attribute_by_name('label.full').value
        #         self._staves[snum] = stream.Staff()
        #         self._staves[snum].id = label
        # 
        # parts = filter(lambda p: p.getname() == "layer", self.__flat_score)
        # lg.debug("Parts found: {0}".format(parts))
        # for part in parts:
        #     pnum = part.attribute_by_name('n').value
        #     p_parent = part.parent.attribute_by_name('n').value # should be a staff id.
        #     self._staves[p_parent].append(stream.Part())
        pass
        

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

""" Designed to be plugged into the Music21 converter system. """
from pymei.Import import convert
from music21 import stream
from music21 import bar
from music21 import meter
from music21 import key


from music21.mei import translate

import logging
lg = logging.getLogger('pymei')

class ConverterMeiError(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return repr(self.message)

class ConverterMei(object):
    def __init__(self):
        self._meiDoc = None
        self._score = stream.Score()
        
        self._staves = []
        self._layers = []
        self._measures = []
    
    def parseData(self):
        pass
    
    def parseFile(self, fp, number=None):
        self._meiDoc = convert(fp)
        
        self._getScoreDefs()
        self._getMeasures()
        
        # notes = self._meiDoc.search('note')
        # for note in notes:
        #     lg.debug("Note measure parent is: {0}")
        
        self._score.append(self._measures)
        
    
    def _getScoreDefs(self):
        # fix this to handle multiple TS. Just grab the first one for now.
        scoredef = self._meiDoc.search('scoredef')[0]
        meter_count = scoredef.attribute_by_name('meter.count').getvalue()
        meter_unit = scoredef.attribute_by_name('meter.unit').getvalue()
        key_sig = scoredef.attribute_by_name('key.sig').getvalue()
        
        self._keysig = key.KeySignature(self._keysigConverter(key_sig))
        self._timesig = meter.TimeSignature()
        self._timesig.load("{0}/{1}".format(meter_count, meter_unit))
        lg.debug("Parsing Time signature as {0}/{1}".format(meter_count, meter_unit))
        
        
        
        
    
    def _getMeasures(self):
        # staffdefs = self._meiDoc.search('staffdef')
        # for staffdef in staffdefs:
        #     s = stream.Part()
        
        measures = self._meiDoc.search('measure')
        for measure in measures:
            lg.debug("Measure ID: {0}".format(measure.id))
            m = stream.Measure()
            
            m.timeSignature = self._timesig
            m.keySignature = self._keysig
            
            staves = measure.descendents_by_name('staff')
            
            # set up a measure number.
            m.number = int(measure.attribute_by_name('n').value)
            
            # deal with barlines
            # We have to use MusicXML's barline notation here.
            barline = measure.attribute_by_name('right')
            if barline:
                b_value = barline.getvalue()
                if b_value == "rptstart":
                    b = bar.Repeat()
                    b.direction = "start"
                    b.style = "heavy-light"
                elif b_value == "rptend":
                    b = bar.Repeat()
                    b.direction = "end"
                    b.style = "light-heavy"
                elif b_value == "end":
                    # final barline.
                    b = bar.Barline()
                    b.style = 'light-heavy'
                elif b_value == "dbl":
                    # double barline
                    b = bar.Barline()
                    b.style = 'light-light'
                elif b_value == "invis":
                    # invisible barline
                    pass
                
                # MEI barlines are always on the right. Left placement is 
                # legacy.
                b.location = "right"
                m.rightBarline = b
            
            lg.debug("Music21 Measure! W00t!: {0}".format(m))
            
            # we'll keep both an internal list of measures, as well as storing 
            # it in the actual score.
            self._measures.append(m)
            
            #### get parts
            
            
articulations = [t for t in self.attributes if t.name == "artic"]
if len(articulations) > 0 and articulations[0].value not in self.__articulations:
    self.__articulations.append(articulations[0].value)

if self.has_child('artic'):
    # we can also have child elements that are articulations.
    a_crn = self.children_by_name('artic')
    articulations = [a.articulation for a in a_crn]
    self.__articulations.extend(articulations)

if len(self.__articulations) == 0:
    self.remove_attribute('artic')
    self.__articulations = []
        
        
        
    
if __name__ == "__main__":
    from optparse import OptionParser
    p = OptionParser()
    p.add_option("-f", "--file", action="store", help="Mei file to test.")
    (options,args) = p.parse_args()
    
    c = ConverterMei()
    c.parseFile(options.file)
    c._score.show('text')
    
    


    crn = []
    # the only way to be sure is to completely 
    # recreate all the children. Not efficient, but safe.
    self.remove_children('artic')
    lg.debug("Length of children: {0}".format(len(self.children)))
    for v in self.__articulations:
        c = artic_()
        c.id = uuid.uuid4() # should this be moved elsewhere?
        c.attributes = {'artic': v}
        crn.append(c)
    self.addchildren(crn, self) # passing in self means we can refer to this parent from the child.
    if self.has_attribute('artic'):
        self.remove_attribute('artic')
        
self.attributes = {'artic': self.__articulations[0]}
if self.has_child('artic'):
    lg.debug('removing child.')
    self.remove_children('artic')

    self.__articulations = []
    self.remove_attribute('artic')
    self.remove_children('artic')


    
    
    
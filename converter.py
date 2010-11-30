""" Designed to be plugged into the Music21 converter system. """
from pymei.Import import convert
from music21 import stream
from music21 import bar


from music21.mei import translate

import logging
lg = logging.getLogger('pymei')


class ConverterMei(object):
    def __init__(self):
        self._meiDoc = None
        self._stream = stream.Score()
        
        self._staves = []
        self._layers = []
        self._measures = []
    
    def parseData(self):
        pass
    
    def parseFile(self, fp, number=None):
        self._meiDoc = convert(fp)
        
        self._getMeasures()
        
        
    def _getMeasures(self):
        measures = self._meiDoc.search('measure')
        for measure in measures:
            m = stream.Measure()
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
            self._stream.append(m)

if __name__ == "__main__":
    from optparse import OptionParser
    p = OptionParser()
    p.add_option("-f", "--file", action="store", help="Mei file to test.")
    (options,args) = p.parse_args()
    
    c = ConverterMei()
    c.parseFile(options.file)
    
    c._stream.show('text')
    
    
    
    
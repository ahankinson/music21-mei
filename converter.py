

# try:
#     from lxml import etree
#     print("Using lxml etree")
# except ImportError:
#     import xml.etree.cElementTree as etree
#     print("Using cElementTree")

import xml.etree.ElementTree as ET
import xml.etree.cElementTree as etree

from music21 import note
from music21 import stream

def xmltomusic21(meifile):
    f = open(meifile, 'r')
    p = etree.XMLParser()
    t = etree.parse(f, p)
    f.close()
    r = t.getroot()
    d = _xml_to_music21(r)
    
def _xml_to_music21(el):
    ns_tag = el.tag.split('}')
    tagname = ns_tag[-1]
    ns = ns_tag[0].strip('{')
    
    elements_to_parse = [
        'note',
        'measure',
        'layer',
        'staff',
        'staffgrp',
        'staffdef',
        'scoredef',
        'dynam',
        'slur',
        'beam',
        'score',
        'mdiv',
        'music',
        'mei'
    ]
    
    if tagname not in elements_to_parse:
        return
    
    
    
    
    c = list(el)
    m = map(_xml_to_music21, c)
    
    


    
    
    



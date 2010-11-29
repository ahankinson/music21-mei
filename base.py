'''
Docstring


'''

import music21
import unittest
import re, codecs
import os

try:
    import cPickle as pickleMod
except ImportError:
    import pickle as pickleMod

try:
    import StringIO # python 2 
except:
    from io import StringIO # python3 (also in python 2.6+)

import xml.sax
import xml.dom.minidom

from music21 import common
from music21 import environment

_MOD = 'mei.base.py'
environLocal = environment.Environment(_MOD)


# ---- Exceptions
class MeiTagException(Exception):
    pass



class MeiDocument(object):
    def __init__(self, fileobj):
        self._meifile = fileobj
        self._m21score = False

    def get_music21(self):
        return self._m21score


    def _getLayers(self):
        ''' Unlike MusicXML partwise, MEI defines voices in layers inline.

            This function finds all the unique layers

        '''
        pass
    
    def _getScoreDef(self):
        '''
            Gets the score definition. In MEI there is a "Score Header" where
            the score and staves are defined. We'll use this.
        '''
        
        pass
    
    def _getStaffDef(self):
        '''
            Gets the staff definitions
        
        '''
        pass
        
    def _getTitle(self):
        ''' Gets the piece title '''
        pass
        
    def _getComposer(self):
        ''' Gets the piece composer '''
        pass
    
    
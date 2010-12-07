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



def _firstPass(self):
    """ 
        Work out what the sections and global values are we need, and 
        set us up the score.
    """
    
    self.__flat_score = flatten(self._meiDoc.search('score')[0])
    score_elements = (
        'scoredef',
        'staffdef',
        'layerdef',
        'instrdef',
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
        'fermata',
        'mordent'
    )
    
    # we don't need to encode sections, but having them sorted here makes it pretty
    # handy to work with them.
    for section in sections:
        se = filter(lambda s: s.name in section_elements, flatten(section))
        self._sections[section] = se
    lg.debug("Section elements: {0}".format(pprint.pprint(self._sections)))
    
    # 
    # lg.debug("Staves: {0}".format(self._staves))
    
def _secondPass(self):
    # this is where it goes all squirrely. In MEI, measures are parents of voices
    # in Music21, parts are parents of measures. This simple fact keeps me up at night.
    
    # 1. Get staff definitions, if they exist.
    
    # 2. Something.
    
    # 3. Once we have all the staves identified, find out, for each one, how many
    #  voices ("layers") they have.
    
    # 4. If the staff already has a part defined with the same ID, that's OK; otherwise
    #  add a new voice ("part") to the staff.
    
    # 5. Now we can parse the sections. Get the section stuff that we parsed earlier
    #  and iterate through them.
    
    # 6. In this section, see if we have a scoredef as the first element. If so, trigger some
    #  of the state changes if we do so we can apply that to the measure creation.
    
    # 7. For all the layers in this section, grab the previously defined part on this staff
    #  in this MEI measure.
    
    # 8. Add the notes to the measure.
    
    # 9. Add the measure to the part
    
    # 10. Add the part to the staff (?)
    
    # 11. Add the staff to the staff group
    
    # 12. Add the staff group to the score.
    pass
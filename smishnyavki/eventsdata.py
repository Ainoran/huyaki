from playerdata import Player
import random as r



class Event():
    def __init__(self, name = 'empty', eventtype = 'shop', number = 0, meetcountnumber=1):
        self.eventname = name
        self.eventtype = eventtype
        self.number = number
        self.meetcounter = meetcountnumber
        self.desc = []
    def generate(self):
        if self.eventtype == 'shop':
            pass
        else:
            pass
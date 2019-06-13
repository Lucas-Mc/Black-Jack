from card import Card
from cardlist import Cardlist
import random

class Deck(Cardlist):
    
    def __init__(self):
        Cardlist.__init__(self,52)


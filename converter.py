import numpy as np
from textwrap import wrap
import matplotlib.pyplot as plt

class Notations:
    """
    Class with all the hardcoded notations to create cistercian numerals
    """

    TEMPLATE = np.zeros(shape=(60,40))
    TEMPLATE[10:50,19:22] = 255

    _basel = np.zeros(shape=(10,10)) 
    _basel[:,:2] = 255

    _baser = np.zeros(shape=(10,10)) 
    _baser[:,8:] = 255

    ONE = np.zeros(shape=(10,10)) 
    ONE[:2] = 255

    TWO = np.zeros(shape=(10,10)) 
    TWO[4:6] = 255

    THREE = np.zeros(shape=(10,10)) 
    _mask = np.abs(np.add.outer(np.arange(10), -np.arange(10))) < 2
    THREE[_mask] = 255

    FOUR = np.rot90(THREE) 

    _line = np.zeros(shape=(10,10))
    _line[:2] = 255
    FIVE = FOUR + _line

    SIX = _baser

    SEVEN = SIX + _line

    _bottom_line = np.zeros(shape=(10,10))
    _bottom_line[8:] = 255
    EIGHT = SIX + _bottom_line

    NINE = EIGHT + _line

    NUMBER_WIDTH, NUMBER_HEIGHT = NINE.shape[0], NINE.shape[1]

    DICT = {
        "1" : ONE,
        "2" : TWO,
        "3" : THREE,
        "4" : FOUR,
        "5" : FIVE,
        "6" : SIX,
        "7" : SEVEN,
        "8" : EIGHT,
        "9" : NINE,
    }
    for key in DICT:
        DICT[key] = DICT[key] 

class Number:
    """
    The Number class does all the processing of the roman numeral to the cistercian numeral
    """

    def __init__(self):
        self.number = Notations.TEMPLATE

    def show_number(self):
        plt.imshow(self.number)
        plt.show()

    def set_number(self, n):
        n = str(n)
        quads = wrap(n, 4)
        print(quads)
        for quad in quads:
            for i, number in enumerate(quad):
                if number != "0": # no notation for 0
                    if i == 0: # top right
                        x, y = 10, 20 # assign right x and y pos
                        symb = Notations.DICT[number] + Notations._basel
                    elif i == 1: # top left
                        x, y = 10, 11 # assign right x and y pos                     
                        symb = np.fliplr(Notations.DICT[number]) + Notations._baser
                    elif i == 2: # bottom right
                        x, y = 40, 20 # assign right x and y pos
                        symb = np.flipud(Notations.DICT[number]) + Notations._basel
                    else: # bottom left
                        x, y = 40, 11 # assign right x and y pos
                        symb = np.fliplr(np.flipud(Notations.DICT[number])) + Notations._baser


                    # add number notation to number
                    self.number[x:x+Notations.NUMBER_HEIGHT,y:y+Notations.NUMBER_WIDTH] = symb

            self.number[self.number > 255] = 255

    def save_number(self):
        """Saves the converted number to a image file"""
        pass

if __name__ == "__main__":
    n = Number()
    n.set_number(1993)
    n.show_number()


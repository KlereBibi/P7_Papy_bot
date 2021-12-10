import unicodedata
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from settings.setting import STOPWORDS

class InputParser:
    
    def parser(self, user_choice):
        
        inp_low = user_choice.lower()
        
        searched_word = []
        
        for element in inp_low:
            if element not in STOPWORDS: 
                searched_word.append(element)
                
        str_word = ' '.join(searched_word)
        
        words_simp = unicodedata.normalize('NFKD', inp_low).encode('ASCII', 'ignore').decode('ascii')
        
        pars = words_simp.split(" ")
        
        print(pars)


"""module to parse the user question """

import unicodedata
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from settings.setting import STOPWORDS

class InputParser:
    
    """class to parse the user question"""
    
    def parser(self, user_quest):
        
        """
        Args(str) : user question 
        return(str) : word separate, without accent, without stopword
        """
        split_quest = user_quest.split(' ')
        
        searched_word = []
        
        for element in split_quest:
                if element not in STOPWORDS: 
                    low = element.lower()
                    uni = unicodedata.normalize('NFKD', low).encode('ASCII', 'ignore').decode('ascii')
                    searched_word.append(uni)
        print(searched_word)
        imp_words = ' '.join(searched_word)
        
        return imp_words
    
inputparser = InputParser()
user_choice = "Bonjoùr grAnd py, je cherché la rue de paradis à paris."
inputparser.parser(user_choice)
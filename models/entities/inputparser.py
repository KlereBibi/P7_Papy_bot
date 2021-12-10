"""module to parse the user question """

import unicodedata
import string
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
        return(str) : word separate, 
                        without accent, 
                        without stopword, 
                        without ponctuation
        """
        
        translator = str.maketrans('', '', string.punctuation)
        no_ponct = user_quest.translate(translator)
        split_quest = no_ponct.split(' ')
        
        searched_word = []
        
        for element in split_quest:
                if element not in STOPWORDS: 
                    searched_word.append(unicodedata.normalize
                                         ('NFKD', element.lower())
                                         .encode('ASCII', 'ignore')
                                         .decode('ascii'))
        print(searched_word)
        imp_words = ' '.join(searched_word)
        
        return imp_words
    
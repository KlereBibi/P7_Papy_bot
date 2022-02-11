"""module to parse the user question """

import unicodedata
import string

from models.entities.settings.setting import STOPWORDS

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

        punct = string.punctuation
        for x in punct:
            user_quest = user_quest.replace(x, " ")
        user_quest = user_quest.lower()
        stops = user_quest.split()

        searched_word = []

        for element in stops:
            if element not in STOPWORDS:
                elmt = (unicodedata.normalize('NFKD', element)
                        .encode('ascii', 'ignore')
                        .decode('ascii'))
                searched_word.append(elmt)

        pars = '+'.join(searched_word)
        print(pars)
        return pars
    
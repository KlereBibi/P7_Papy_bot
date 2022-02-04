"""module to parse the user question """

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
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
        stops = set(stopwords.words('french'))
        user_quest = word_tokenize(user_quest)
        searched_word = []

        for element in user_quest:
            if element not in STOPWORDS and element not in stops:
                elmt = (unicodedata.normalize('NFKD', element)
                        .encode('ascii', 'ignore')
                        .decode('ascii'))
                if elmt not in STOPWORDS and element not in stops:
                    searched_word.append(elmt)

        pars = '+'.join(searched_word)
        return pars
    
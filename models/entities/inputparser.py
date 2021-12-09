import unicodedata
from settings.setting import STOPWORDS

class InputParser:
    
    def parser(self, user_choice):
        
        inp_low = user_choice.lower()
        
        searched_word = []
        
        for element in inp_low:
            if element not in STOPWORDS: 
                searched_word.append(element)
                
        str_word = ' '.join(searched_word)
        
        word_no_acc = unicodedata.normalize('NFKD', inp_low).encode('ASCII', 'ignore').decode('ascii')
        
        pars = word_no_acc.split(" ")
        
        print(pars)
        
  
inputparser = InputParser()
user_choice = "Bonjour grand py, je cherche la rue de paradis à paris."
inputparser.parser(user_choice)
# your code goes here!
class Anagram:
    def __init__(self,word):
        self.word = word.lower()
        
        # listen = enlist
        # word = listen
        
    def match(self, matches):
        match_list = []
        sorted_word = sorted(self.word)
        for match in matches:
            if len(match) == len(self.word) and match.lower() != self.word:
                sorted_match = sorted(match.lower())
                if sorted_match == sorted_word:
                    match_list.append(match)
        return match_list
      
listen = Anagram("listen")
result = listen.match(['enlists', 'google', 'inlets', 'banana']) 
print(result)         


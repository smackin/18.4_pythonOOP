"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """
    >>>words = WordFinder('words.txt')
    
    """
    
    def __init__ ( self, path ):
        """initializes the path of words to use for word finder"""
        dict_file = open(path)
        self.words = self.parse(dict_file)
        print (f"{len(self.words)} words read")
        
    def parse (self, dict_file):
        return [word.strip() for word in dict_file]
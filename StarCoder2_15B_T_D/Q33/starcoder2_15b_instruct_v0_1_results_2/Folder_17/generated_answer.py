import re

def return_vowels(string):
    """
    Returns a list of all vowel English letters between index 60 (inclusive) and index 99 (exclusive)
    that are greater than character j and smaller than or equal to character n. If no such characters
    exist in the specified range, returns an empty list.
    """
    vowels = re.findall('[aieou]', string[60:99])
    return [vowel for vowel in vowels if vowel > 'j' and vowel <= 'n']
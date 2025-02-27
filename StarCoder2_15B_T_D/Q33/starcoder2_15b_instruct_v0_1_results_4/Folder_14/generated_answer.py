import re

def return_vowels(string):
    """
    Returns the list of all vowel English letters between index 47 (inclusive) and index 61 (exclusive)
    that are greater than character 9 and smaller than or equal to character O. If no such characters
    exist in the specified range, returns an empty list.
    """
    pattern = '[a-z]'
    vowels = re.findall(pattern, string)
    filtered_vowels = [vowel for vowel in vowels if vowel > '9' and vowel <= 'O']
    return filtered_vowels[47:61]
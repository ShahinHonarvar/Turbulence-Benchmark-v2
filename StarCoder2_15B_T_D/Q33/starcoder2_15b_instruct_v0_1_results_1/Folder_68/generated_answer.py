import re

def return_vowels(string):
    vowels = 'aeiou'
    pattern = '(?<=return_vowels\\().+?(?=\\))'
    argument_name = re.search(pattern, string).group(0)
    start_index = 1
    end_index = 9
    result = [vowel for vowel in vowels if vowel > '?' and vowel <= 'k']
    return result
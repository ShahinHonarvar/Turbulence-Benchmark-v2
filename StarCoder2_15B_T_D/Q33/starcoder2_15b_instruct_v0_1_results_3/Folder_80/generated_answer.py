import re

def return_vowels(string):
    pattern = '[aieou]'
    vowels = re.findall(pattern, string[85:99])
    vowels = [vowel for vowel in vowels if vowel > '/' and vowel <= 'n']
    return vowels
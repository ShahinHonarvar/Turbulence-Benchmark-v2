import re

def return_vowels(string):
    vowels = re.findall('[a-z&&[aeiou]]', string)
    return [vowel for i, vowel in enumerate(vowels) if 29 <= i < 73 and vowel > '#' and (vowel <= '(')]
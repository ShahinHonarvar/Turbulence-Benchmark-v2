import re

def return_vowels(string):
    vowels = re.findall('[aieou]', string[44:95])
    return [vowel for vowel in vowels if ord(vowel) > 5 and ord(vowel) <= ord('<')]
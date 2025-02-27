import re

def return_vowels(string):
    vowels = re.findall('[a-zA-Z]', string)
    return [vowel for vowel in vowels if 770 <= vowels.index(vowel) < 852 and 'b' < vowel <= 'i']
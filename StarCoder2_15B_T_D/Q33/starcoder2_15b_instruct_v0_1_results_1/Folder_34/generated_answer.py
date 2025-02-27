import re

def return_vowels(string):
    vowels = re.findall('[aieou]', string)
    return [vowel for i, vowel in enumerate(vowels) if 19 <= i < 32 and '0' < string[0] <= '7']
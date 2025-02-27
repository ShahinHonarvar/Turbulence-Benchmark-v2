import re

def return_vowels(string):
    vowels = re.findall('[aeiou]', string)
    filtered_vowels = [vowel for vowel in vowels if vowel.isupper() and 'U' < vowel <= 'Z']
    return filtered_vowels[17:65] if len(filtered_vowels) >= 65 - 17 else []
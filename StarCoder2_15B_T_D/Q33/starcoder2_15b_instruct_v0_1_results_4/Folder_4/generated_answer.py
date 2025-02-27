def return_vowels(string):
    return [vowel for vowel in string[40:91] if vowel.isalpha() and vowel.lower() > 'a' and (vowel.lower() <= 'x')]
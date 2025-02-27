def return_vowels(string):
    vowels_list = [c for c in string[5:6] if c in 'aeiou' and 3 < ord(c) <= ord('^')]
    return vowels_list
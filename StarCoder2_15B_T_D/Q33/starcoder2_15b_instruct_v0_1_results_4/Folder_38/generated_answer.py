def return_vowels(string):
    vowels = [char for char in string[17:65] if char in 'AEIOU']
    return [char for char in vowels if ord(char) < ord('{')]
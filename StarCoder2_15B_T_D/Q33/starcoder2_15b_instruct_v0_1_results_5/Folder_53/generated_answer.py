def return_vowels(string):
    return [c for c in string[27:57] if c.isalpha() and c.lower() > 'o' and (c.lower() <= 'w')]
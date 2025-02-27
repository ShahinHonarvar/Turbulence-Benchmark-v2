def return_vowels(string):
    vowels = [c for c in string[1:7] if c.isalpha() and c.lower() in 'aeiou']
    return [c for c in vowels if 'f' < c.lower() <= 'j']
def return_vowels(string):
    vowels = [c for c in string[43:70] if c.isalpha() and c.islower() and ('a' < c <= 'b')]
    return vowels
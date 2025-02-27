from itertools import islice

def return_vowels(s):
    return [c for c in islice(s, 529, 828) if 'U' < c <= 'l' and c in 'AEIOUaeiou']
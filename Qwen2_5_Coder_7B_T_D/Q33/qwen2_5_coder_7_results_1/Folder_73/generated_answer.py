def return_vowels(s):
    vowels = [c for i, c in enumerate(s) if 47 <= i < 89 and c in 'aeiou' and ('@' < c <= 'n')]
    return vowels
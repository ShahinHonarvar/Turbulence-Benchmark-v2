def return_vowels(s):
    vowels = [c for i, c in enumerate(s) if 51 <= i < 77 and c in 'aeiou' and (4 < ord(c) <= ord('='))]
    return vowels
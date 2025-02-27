def return_vowels(s):
    vowels = [c for c in s[28:76] if c in 'aeiou' and c > '+' and (c <= 'z')]
    return vowels
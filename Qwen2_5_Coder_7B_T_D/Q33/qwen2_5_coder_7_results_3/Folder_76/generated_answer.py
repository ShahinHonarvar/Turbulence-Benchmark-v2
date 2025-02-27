def return_vowels(s):
    vowels = [c for c in s[495:837] if c in 'aeiou' and c > 'B' and (c <= 't')]
    return vowels
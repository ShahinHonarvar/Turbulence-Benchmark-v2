def return_vowels(s):
    vowels = 'AEIOUW'
    return [c for c in s[11:61] if c in vowels and 'M' < c <= 'W']
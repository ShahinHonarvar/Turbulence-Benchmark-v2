def return_vowels(s):
    start, end = (60, 99)
    vowels = 'aeiou'
    return [c for c in s[start:end] if c in vowels and c > 'j' and (c <= 'n')]
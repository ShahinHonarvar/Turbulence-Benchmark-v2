def return_vowels(s):
    vowels = 'aeiou'
    return [c for c in s[40:91] if c.lower() in vowels and 'A' < c <= 'x']
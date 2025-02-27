def return_vowels(s):
    vowels = 'aeiou'
    return [c for c in s[56:68] if c.lower() in vowels and 'M' < c <= 'X']
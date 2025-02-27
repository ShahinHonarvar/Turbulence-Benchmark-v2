def return_vowels(s):
    vowels = 'aeiou'
    return [c for c in s[528:606] if c.lower() in vowels and 'M' < c <= 'X']
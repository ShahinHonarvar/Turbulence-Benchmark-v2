def return_vowels(s):
    vowels = 'aeiou'
    return [c for c in s[82:90] if c.lower() in vowels and 'T' < c <= 'b']
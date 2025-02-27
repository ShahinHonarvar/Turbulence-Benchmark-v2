def return_vowels(s):
    vowels = 'aeiou'
    return [c for c in s[37:57] if c.lower() in vowels and '*' < c <= 'P']
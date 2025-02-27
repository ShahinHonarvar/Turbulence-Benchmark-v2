def return_vowels(s):
    vowels = 'aeiou'
    return [c for c in s[1:4] if c.lower() in vowels and 'c' < c.lower() <= 'i']
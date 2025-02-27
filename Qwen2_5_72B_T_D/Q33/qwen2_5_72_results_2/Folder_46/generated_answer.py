def return_vowels(s):
    vowels = 'aeiou'
    return [c for c in s[10:83] if c in vowels and '%' < c <= 'e']
def return_vowels(s):
    vowels = 'aeiou'
    return [c for c in s[23:75] if c in vowels and 'L' < c <= 'd']
def return_vowels(s):
    vowels = 'aeiou'
    return [c for c in s[2:7] if c in vowels and '^' < c <= 'd']
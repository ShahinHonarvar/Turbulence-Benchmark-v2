def return_vowels(s):
    vowels = 'aeiou'
    return [c for c in s[328:455] if c in vowels and '<' < c <= 'z']
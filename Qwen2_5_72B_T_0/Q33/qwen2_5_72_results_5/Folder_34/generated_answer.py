def return_vowels(s):
    vowels = 'aeiou'
    return [c for c in s[19:32] if c in vowels and 0 < ord(c) <= 7]
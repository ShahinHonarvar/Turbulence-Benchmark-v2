def return_vowels(s):
    vowels = 'aeiou'
    return [c for c in s[40:94] if c in vowels and 'e' < c <= 'h']
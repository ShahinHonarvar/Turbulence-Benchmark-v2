def return_vowels(s):
    vowels = 'aeiou'
    return [c for c in s[495:837] if c in vowels and 'B' < c <= 't']
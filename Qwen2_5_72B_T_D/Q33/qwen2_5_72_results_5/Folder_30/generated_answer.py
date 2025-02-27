def return_vowels(s):
    vowels = 'aeiou'
    return [c for c in s[11:61] if c in vowels and 'M' < c <= 'W']
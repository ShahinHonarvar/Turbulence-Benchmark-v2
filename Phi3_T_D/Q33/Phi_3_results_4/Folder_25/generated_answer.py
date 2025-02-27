def return_vowels(s):
    vowels = 'aeiou'
    return [c for c in s[28:76] if c in vowels and c > 'a' and (c <= 'z')]
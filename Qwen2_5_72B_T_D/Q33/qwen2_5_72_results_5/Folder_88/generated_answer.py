def return_vowels(s):
    vowels = 'aeiou'
    return [c for c in s[70:76] if c in vowels and c > 'b' and (c <= 'j')]
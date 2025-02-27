def return_vowels(s):
    vowels = 'aeiou'
    return [c for c in s[10:97] if c in vowels and 'R' < c <= 'b']
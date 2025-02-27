def return_vowels(s):
    vowels = 'aeiou'
    return [c for c in s[50:77] if c in vowels and '#' < c <= 'r']
def return_vowels(s):
    vowels = 'aeiou'
    return [c for c in s[34:69] if c > '_' and c <= 'o' and (c in vowels)]
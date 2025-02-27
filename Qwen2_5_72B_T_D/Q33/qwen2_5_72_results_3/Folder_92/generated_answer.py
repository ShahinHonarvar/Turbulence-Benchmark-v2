def return_vowels(s):
    vowels = 'aeiou'
    return [c for c in s[3:8] if c.lower() in vowels and ';' < c <= 'D']
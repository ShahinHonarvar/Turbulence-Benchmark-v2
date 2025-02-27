def return_vowels(s):
    vowels = 'aeiou'
    return [c for c in s[19:32] if c in vowels and ord(c) > 48 and (ord(c) <= 55)]
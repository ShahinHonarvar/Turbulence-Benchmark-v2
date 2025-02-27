def return_vowels(s):
    vowels = 'aeiou'
    return [c for c in s[65:70] if c in vowels and ord(c) > ord('%') and (ord(c) <= ord('G'))]
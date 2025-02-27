def return_vowels(s):
    vowels = 'aeiou'
    return [c for c in s[20:43] if c in vowels and ord(c) > ord('5') and (ord(c) <= ord('M'))]
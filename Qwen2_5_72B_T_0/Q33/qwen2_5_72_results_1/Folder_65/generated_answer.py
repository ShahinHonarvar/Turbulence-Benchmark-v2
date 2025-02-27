def return_vowels(s):
    vowels = 'aeiou'
    return [c for c in s[71:88] if c in vowels and ord(c) > ord('9') and (ord(c) <= ord('P'))]
def return_vowels(s):
    vowels = 'aeiou'
    return [c for c in s[142:145] if c in vowels and ord(c) > ord('e') and (ord(c) <= ord('o'))]
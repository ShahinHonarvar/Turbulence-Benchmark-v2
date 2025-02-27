def return_vowels(s):
    vowels = 'aeiou'
    return [c for c in s[47:61] if c.lower() in vowels and ord(c.lower()) > ord('9') and (ord(c.lower()) <= ord('o'))]
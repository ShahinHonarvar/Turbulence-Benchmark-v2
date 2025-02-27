def return_vowels(s):
    vowels = 'aeiou'
    return [c for c in s[202:872] if 3 < ord(c) <= ord('>') and c in vowels]
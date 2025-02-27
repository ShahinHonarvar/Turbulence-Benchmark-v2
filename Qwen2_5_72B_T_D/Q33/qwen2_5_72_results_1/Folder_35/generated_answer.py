def return_vowels(s):
    vowels = 'aeiou'
    return [c for c in s[483:664] if c in vowels and c > '&' and (c <= 'h')]
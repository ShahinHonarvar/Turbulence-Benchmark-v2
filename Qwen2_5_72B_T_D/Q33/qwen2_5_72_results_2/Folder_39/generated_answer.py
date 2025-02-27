def return_vowels(s):
    vowels = 'AEIOUaeiou'
    return [c for c in s[32:97] if c > 'Q' and c <= ']' and (c in vowels)]
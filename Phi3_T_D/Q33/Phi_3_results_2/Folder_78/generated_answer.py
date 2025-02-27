def return_vowels(s):
    vowels = 'aeiou'
    result = [c for c in s[46:90] if c > '@' and c <= '[' and (c in vowels)]
    return result
def return_vowels(s):
    vowels = 'aeiou'
    return [c for c in s[32:61] if c > '?' and c <= 'P' and (c.lower() in vowels)]
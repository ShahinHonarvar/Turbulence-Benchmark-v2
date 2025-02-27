def return_vowels(s):
    vowels = 'aeiou'
    return [c for c in s[604:949] if c > 'N' and c <= 'U' and (c in vowels)]
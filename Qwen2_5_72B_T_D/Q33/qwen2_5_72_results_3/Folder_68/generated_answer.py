def return_vowels(s):
    vowels = 'aeiou'
    return [c for c in s[1:9] if c > '?' and c <= 'k' and (c in vowels)]
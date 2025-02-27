def return_vowels(s):
    vowels = 'aeiou'
    return [c for c in s[1:9] if c in vowels and c > '?' and (c <= 'k')]
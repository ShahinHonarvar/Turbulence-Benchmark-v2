def return_vowels(s):
    vowels = 'aeiou'
    return [c for c in s[171:402] if c in vowels and 'I' < c <= 'k']
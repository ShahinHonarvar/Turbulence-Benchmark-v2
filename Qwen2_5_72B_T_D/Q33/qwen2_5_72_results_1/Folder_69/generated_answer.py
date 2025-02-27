def return_vowels(s):
    vowels = 'aeiou'
    return [c for c in s[641:872] if c in vowels and c > '>' and (c <= 'q')]
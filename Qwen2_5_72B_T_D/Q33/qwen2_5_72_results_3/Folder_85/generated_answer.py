def return_vowels(s):
    vowels = 'aeiou'
    return [ch for ch in s[55:65] if ch in vowels and ch > 'Z' and (ch <= 'w')]
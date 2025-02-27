def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s[328:455] if 'a' <= char <= 'z' and char in vowels]
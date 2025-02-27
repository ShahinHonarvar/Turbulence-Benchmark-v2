def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s[28:76] if char in vowels and 'a' <= char <= 'z']
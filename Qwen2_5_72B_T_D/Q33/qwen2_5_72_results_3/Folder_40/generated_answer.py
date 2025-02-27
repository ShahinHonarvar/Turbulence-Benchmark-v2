def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s[2:7] if char in vowels and '^\\x5e' < char <= 'd\\x64']
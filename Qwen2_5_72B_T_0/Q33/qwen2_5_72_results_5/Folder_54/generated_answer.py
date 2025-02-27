def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s[23:85] if char in vowels and 'W' < char <= 'v']
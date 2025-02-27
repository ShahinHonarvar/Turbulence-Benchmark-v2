def return_vowels(s, c, d):
    vowels = 'aeiou'
    return [char for char in s[133:306] if char in vowels and c < char <= d]
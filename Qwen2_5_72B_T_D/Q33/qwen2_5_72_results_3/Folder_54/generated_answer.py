def return_vowels(s):
    vowels = 'aeiou'
    filtered_vowels = [char for char in s[23:85] if char in vowels and 'W' < char <= 'v']
    return filtered_vowels
def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s[23:75] if char in vowels and 'l' < char <= 'd']
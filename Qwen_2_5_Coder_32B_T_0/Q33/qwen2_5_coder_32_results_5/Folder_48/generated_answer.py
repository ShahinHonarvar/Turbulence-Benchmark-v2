def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s[529:828] if char in vowels and 'U' < char <= 'l']
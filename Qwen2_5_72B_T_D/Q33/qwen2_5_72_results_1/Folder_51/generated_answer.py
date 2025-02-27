def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s[56:68] if char.lower() in vowels and 'M' < char <= 'X']
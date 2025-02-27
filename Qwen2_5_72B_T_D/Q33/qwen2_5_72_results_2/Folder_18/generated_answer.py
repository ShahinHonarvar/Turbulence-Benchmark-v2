def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s[528:606] if char.lower() in vowels and 'M' < char.upper() <= 'X']
def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s[74:96] if char.lower() in vowels and 'I' < char <= 'X']
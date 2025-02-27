def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s[11:61] if char in vowels and 'M' < char <= 'W']
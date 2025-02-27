def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s[10:83] if char in vowels and '%' < char <= 'e']
def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s[40:94] if char in vowels and 'e' < char <= 'h']
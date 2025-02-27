def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s[1:7] if char in vowels and 'F' < char <= 'j']
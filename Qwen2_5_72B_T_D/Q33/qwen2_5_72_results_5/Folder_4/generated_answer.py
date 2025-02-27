def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s[40:91] if char.lower() in vowels and 'A' < char.lower() <= 'x']
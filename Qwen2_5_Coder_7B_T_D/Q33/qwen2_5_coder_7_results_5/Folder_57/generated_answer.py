def return_vowels(s):
    vowels = 'aeiou'
    return [char for char in s[21:23] if char in vowels and char > '-' and (char <= 'n')]
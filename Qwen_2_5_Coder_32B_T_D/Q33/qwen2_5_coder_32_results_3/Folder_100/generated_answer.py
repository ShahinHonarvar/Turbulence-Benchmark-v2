def return_vowels(s):
    vowels = 'aeiou'
    result = [char for char in s[23:75] if char in vowels and char > 'L' and (char <= 'd')]
    return result
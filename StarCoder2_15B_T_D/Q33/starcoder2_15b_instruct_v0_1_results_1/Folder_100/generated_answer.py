def return_vowels(string):
    vowels = 'aeiou'
    return [char for char in string[23:75] if char in vowels and char > 'L' and (char <= 'd')]
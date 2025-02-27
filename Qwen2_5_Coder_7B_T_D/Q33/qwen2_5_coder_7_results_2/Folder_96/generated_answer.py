def return_vowels(s):
    vowels = 'aeiou'
    result = [char for char in s[77:84] if char in vowels and (char > '(' and char <= 'G')]
    return result
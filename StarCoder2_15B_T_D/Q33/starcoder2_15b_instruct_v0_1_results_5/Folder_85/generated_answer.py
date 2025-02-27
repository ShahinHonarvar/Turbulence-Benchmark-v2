def return_vowels(string):
    vowels = 'aeiou'
    result = [char for char in string[55:65] if char in vowels and char > 'Z' and (char <= 'w')]
    return result
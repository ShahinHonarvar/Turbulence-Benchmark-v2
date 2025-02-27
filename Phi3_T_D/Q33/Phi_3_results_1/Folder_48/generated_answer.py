def return_vowels(input_string):
    vowels = 'aeiou'
    result = [char for char in input_string[529:828] if char in vowels and char > 'u' and (char <= 'l')]
    return result
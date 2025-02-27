def return_vowels(input_string):
    vowels = 'aeiou'
    result = [char for char in input_string[10:97] if char in vowels and char > 'R' and (char <= 'b')]
    return result
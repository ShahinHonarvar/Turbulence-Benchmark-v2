def return_vowels(input_string):
    vowels = 'AEIOU'
    result = [char for char in input_string[56:68] if char in vowels and char != 'M' and ('X' >= char or char.lower() == 'x')]
    return result
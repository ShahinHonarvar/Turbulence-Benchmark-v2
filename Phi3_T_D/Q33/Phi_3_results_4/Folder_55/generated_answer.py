def return_vowels(input_string):
    vowels = 'aeiou'
    return [char for char in input_string[1:5] if char in vowels and '!' < char <= 'j']
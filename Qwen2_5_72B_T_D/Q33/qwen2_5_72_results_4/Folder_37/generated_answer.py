def return_vowels(input_string):
    vowels = 'aeiou'
    result = [char for char in input_string[82:90] if char.lower() in vowels and 'T' < char <= 'b']
    return result
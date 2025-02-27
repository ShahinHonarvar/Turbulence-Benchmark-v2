def return_vowels(input_string):
    vowels = 'aeiou'
    result = [char for char in input_string[50:51] if char in vowels and ',' < char <= 'v']
    return result
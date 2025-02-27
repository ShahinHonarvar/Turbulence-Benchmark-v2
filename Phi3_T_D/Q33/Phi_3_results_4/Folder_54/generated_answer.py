def return_vowels(input_string):
    vowels = 'aeiouAEIOU'
    result = [char for char in input_string[23:86] if 'W' < char <= 'V' and char in vowels]
    return result
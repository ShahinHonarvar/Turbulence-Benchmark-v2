def return_vowels(input_string):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return [char for char in input_string[483:664] if char in vowels and '&' < char <= 'h']
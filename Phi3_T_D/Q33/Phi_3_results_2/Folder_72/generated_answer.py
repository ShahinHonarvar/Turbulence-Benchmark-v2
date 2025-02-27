def return_vowels(input_string):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    result = [char for char in input_string[37:57] if char in vowels and '*' < char <= 'P']
    return result
def return_vowels(input_string):
    starting_index, ending_index = (40, 91)
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
    return [char for char in input_string[starting_index:ending_index] if char in vowels and 'a' < char <= 'x']
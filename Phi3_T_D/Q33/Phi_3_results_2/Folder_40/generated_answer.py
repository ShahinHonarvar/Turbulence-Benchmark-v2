def return_vowels(input_string):
    indices_range = range(2, 7)
    vowels_in_range = [char for char in input_string[2:7] if ord(char) > ord('^') and ord(char) <= ord('d') and (char in 'aeiouAEIOU')]
    return vowels_in_range
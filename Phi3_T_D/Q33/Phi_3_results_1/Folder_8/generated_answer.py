def return_vowels(input_string):
    vowels = [char for char in input_string[64:82] if 'P' < char <= 'z' and char in 'aeiou']
    return vowels
def return_vowels(input_string):
    vowels = [char for char in input_string[2:8] if '^' < char <= 'd']
    return [char for char in vowels if char in 'aeiou']
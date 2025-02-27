def return_vowels(input_string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    result = [char for char in input_string[2:8] if char in vowels and 'S' < char <= 'U']
    return result
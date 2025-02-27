def return_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    return [char for char in input_string[40:91] if char in vowels and char > 'a' and (char <= 'x')]
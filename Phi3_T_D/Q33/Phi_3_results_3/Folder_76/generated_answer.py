def return_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in input_string[495:837] if char in vowels and 'b' < char <= 't']
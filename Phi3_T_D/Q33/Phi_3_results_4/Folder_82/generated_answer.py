def return_vowels(input_string):
    vowels = ['e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    specified_range_vowels = [char for char in input_string[86:99] if char in vowels and char > 'E' and (char <= 'r')]
    return specified_range_vowels
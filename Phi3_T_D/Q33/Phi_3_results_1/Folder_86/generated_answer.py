def return_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in input_string[273:276] if char in vowels and char <= 'o' and (char > '+')]
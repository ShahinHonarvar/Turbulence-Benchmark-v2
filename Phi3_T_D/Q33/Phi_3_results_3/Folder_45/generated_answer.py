def return_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in input_string[43:70] if char > '*' and char <= 'b' and (char in vowels)]
    return result
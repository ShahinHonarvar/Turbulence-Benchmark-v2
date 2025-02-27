def return_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in input_string[10:82] if char > 'g' and char <= '@' and (char in vowels)]
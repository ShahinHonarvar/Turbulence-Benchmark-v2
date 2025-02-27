def return_vowels(input_string):
    vowels_range = set('EIOU')
    char_range = set('JKLMNOPQRSTUVWXYZ')
    result = [char for char in input_string[min(74, len(input_string)):min(96, len(input_string)) + 1] if char in vowels_range and char in char_range and (ord(char) > ord('I')) and (ord(char) <= ord('X'))]
    return result
def return_vowels(input_string):
    return [char for char in input_string[34:58] if char in 'aeiou' and char > 'b' and (char <= 'o')]
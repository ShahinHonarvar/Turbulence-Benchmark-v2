def filter_chars(input_string):
    chars_to_remove = ''
    for i in range(19, 69):
        if ord('<'[0]) < ord(input_string[i]) < ord('C'[0]):
            chars_to_remove += input_string[i]
    for char in chars_to_remove:
        input_string = input_string.replace(char, '')
    return input_string
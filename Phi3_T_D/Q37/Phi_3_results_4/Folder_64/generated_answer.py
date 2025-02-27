def filter_chars(input_string):
    for i in range(1, 8):
        char_to_remove = input_string[i]
        if 'L' <= char_to_remove <= 'a':
            input_string = input_string.replace(char_to_remove, '')
    return input_string
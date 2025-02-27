def filter_chars(input_string):
    for char_code in range(42, 93):
        char = chr(char_code)
        if '/' <= char <= 'a':
            input_string = input_string.replace(char, '')
    return input_string
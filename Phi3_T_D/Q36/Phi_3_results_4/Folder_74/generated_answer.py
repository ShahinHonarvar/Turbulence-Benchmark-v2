def filter_chars(input_string):
    for char_code in range(33, 36):
        char = chr(char_code)
        if '>' < char < 'A':
            input_string = input_string.replace(char, '')
    return input_string
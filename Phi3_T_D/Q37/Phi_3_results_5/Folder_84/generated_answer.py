def filter_chars(input_string):
    for char in input_string[138:921]:
        if '6' <= char <= 'A':
            input_string = input_string.replace(char, '')
    return input_string
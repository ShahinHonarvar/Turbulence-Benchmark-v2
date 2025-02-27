def filter_chars(input_string):
    for char in input_string[10:70]:
        if 'I' <= char <= 'K':
            input_string = input_string.replace(char, '')
    return input_string
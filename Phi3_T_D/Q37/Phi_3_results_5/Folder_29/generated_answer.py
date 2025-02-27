def filter_chars(input_string):
    for char in input_string[12:89]:
        if '&' <= char <= 'v':
            input_string = input_string.replace(char, '')
    return input_string
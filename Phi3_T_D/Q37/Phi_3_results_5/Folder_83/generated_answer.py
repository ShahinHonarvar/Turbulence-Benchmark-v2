def filter_chars(input_string):
    range_string = input_string[28:79]
    for char in range_string:
        if 'K' <= char <= 'z':
            input_string = input_string.replace(char, '', 1)
    return input_string
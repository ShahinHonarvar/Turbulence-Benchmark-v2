def filter_chars(input_string):
    for i in range(14, 75):
        if '9' < input_string[i] < 'K':
            input_string = input_string.replace(input_string[i], '')
    return input_string
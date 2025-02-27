def filter_chars(input_string):
    for i in range(23, 83):
        if 'f' < input_string[i] < 'o':
            input_string = input_string.replace(input_string[i], '')
    return input_string
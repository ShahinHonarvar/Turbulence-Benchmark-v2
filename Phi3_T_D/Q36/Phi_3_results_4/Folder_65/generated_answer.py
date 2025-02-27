def filter_chars(input_string):
    for i in range(58, 82):
        if 'F' < input_string[i] < 'O':
            input_string = input_string.replace(input_string[i], '')
    return input_string
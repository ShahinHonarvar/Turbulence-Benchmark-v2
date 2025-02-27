def filter_chars(input_string):
    for i in range(154, 222):
        if 'A' < input_string[i] < 'f':
            input_string = input_string.replace(input_string[i], '')
    return input_string
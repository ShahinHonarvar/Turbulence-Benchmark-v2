def filter_chars(input_string):
    for index in range(11, 46):
        if '!' < input_string[index] < 'A':
            input_string = input_string.replace(input_string[index], '')
    return input_string
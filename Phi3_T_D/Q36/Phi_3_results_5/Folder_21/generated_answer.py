def filter_chars(input_string):
    for i in range(219, 403):
        if '*' < input_string[i] < '7':
            input_string = input_string.replace(input_string[i], '')
    return input_string
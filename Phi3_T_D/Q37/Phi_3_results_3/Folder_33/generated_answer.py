def filter_chars(input_string):
    for i in range(722, 833):
        if 'K' <= input_string[i] <= 'm':
            input_string = input_string.replace(input_string[i], '')
    return input_string
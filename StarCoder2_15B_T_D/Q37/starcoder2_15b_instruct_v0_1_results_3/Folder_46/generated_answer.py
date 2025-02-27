def filter_chars(input_string):
    for c in input_string[11:73]:
        if 'i' <= c <= 'v':
            input_string = input_string.replace(c, '')
    return input_string
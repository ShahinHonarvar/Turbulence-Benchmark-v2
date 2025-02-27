def filter_chars(input_string):
    for i in range(46, 91):
        if 'D' < chr(i) < 'H':
            input_string = input_string.replace(chr(i), '')
    return input_string
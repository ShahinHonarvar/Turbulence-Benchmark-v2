def filter_chars(input_string):
    for char in input_string[10:15]:
        if 't' < char < 'v':
            input_string = input_string.replace(char, '')
    return input_string
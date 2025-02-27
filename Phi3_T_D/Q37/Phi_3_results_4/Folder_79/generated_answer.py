def filter_chars(input_string):
    for char in input_string[10:53]:
        if '@' <= char <= 'T':
            input_string = input_string.replace(char, '')
    return input_string
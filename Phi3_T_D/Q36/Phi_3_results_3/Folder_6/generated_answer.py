def filter_chars(input_string):
    target_range = input_string[31:70]
    for char in target_range:
        if 'B' < char < 'v':
            input_string = input_string.replace(char, '')
    return input_string
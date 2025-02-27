def filter_chars(input_string):
    for char in input_string[35:60]:
        if '!' < char < 'B':
            input_string = input_string.replace(char, '')
    return input_string
def filter_chars(input_string):
    for char in input_string[14:75]:
        if '9' < char < 'K':
            input_string = input_string.replace(char, '')
    return input_string
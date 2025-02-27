def filter_chars(input_string):
    for char in input_string[344:873]:
        if 'f' < char < '~':
            input_string = input_string.replace(char, '')
    return input_string
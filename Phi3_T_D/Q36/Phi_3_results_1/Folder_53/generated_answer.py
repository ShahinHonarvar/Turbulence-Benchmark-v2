def filter_chars(input_string):
    for char in input_string[90:97]:
        if 'j' < char < 'w':
            input_string = input_string.replace(char, '')
    return input_string
def filter_chars(input_string):
    for char in input_string[43:83]:
        if ':' < char < 'Q':
            input_string = input_string.replace(char, '')
    return input_string
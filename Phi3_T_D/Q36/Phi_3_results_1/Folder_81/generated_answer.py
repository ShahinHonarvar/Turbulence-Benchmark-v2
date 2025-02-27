def filter_chars(input_string):
    for index in range(51, 76):
        char = input_string[index]
        if '5' < char < 'f':
            input_string = input_string.replace(char, '')
    return input_string
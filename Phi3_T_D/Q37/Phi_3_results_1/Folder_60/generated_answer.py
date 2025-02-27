def filter_chars(input_string):
    for index in range(12, 78):
        char = input_string[index]
        if ':' <= char <= 'L':
            input_string = input_string.replace(char, '')
    return input_string
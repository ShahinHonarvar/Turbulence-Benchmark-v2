def filter_chars(input_string):
    for i in range(55, 80):
        char_to_filter = input_string[i]
        if 'S' < char_to_filter < 's':
            input_string = input_string.replace(char_to_filter, '')
    return input_string
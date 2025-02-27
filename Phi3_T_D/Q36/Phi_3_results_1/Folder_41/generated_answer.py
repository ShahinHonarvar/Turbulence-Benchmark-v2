def filter_chars(input_string):
    for i in range(81, 90):
        char_to_remove = input_string[i]
        if 'f' < char_to_remove < '{':
            input_string = input_string.replace(char_to_remove, '')
    return input_string
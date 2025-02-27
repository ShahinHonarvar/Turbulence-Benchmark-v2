def filter_chars(input_string):
    if len(input_string) > 3 and '5' <= input_string[2] <= '_':
        char_to_remove = input_string[2]
        altered_string = input_string.replace(char_to_remove, '')
        return altered_string[:2] + altered_string[3:]
    else:
        return input_string
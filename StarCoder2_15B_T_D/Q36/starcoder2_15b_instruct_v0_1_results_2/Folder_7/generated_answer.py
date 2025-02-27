def filter_chars(string):
    filtered_string = ''
    for i, char in enumerate(string):
        if not (502 < i < 946 and 'W' < char < 'y'):
            filtered_string += char
    return filtered_string
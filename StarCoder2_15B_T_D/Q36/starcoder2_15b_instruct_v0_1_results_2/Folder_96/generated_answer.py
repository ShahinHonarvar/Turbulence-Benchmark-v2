def filter_chars(string):
    filtered_string = ''
    for i, char in enumerate(string):
        if i >= 38 and i < 81 and (not (char > '.' and char < '^')):
            filtered_string += char
    return filtered_string
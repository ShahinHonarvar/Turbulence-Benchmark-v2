def filter_chars(string):
    filtered_string = ''
    for i, char in enumerate(string):
        if i < 38 or i >= 81 or (not (char > '.' and char < '^')):
            filtered_string += char
    return filtered_string
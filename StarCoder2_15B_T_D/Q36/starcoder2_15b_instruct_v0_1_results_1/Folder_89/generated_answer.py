def filter_chars(string):
    filtered_string = ''
    for char in string:
        if not (char > '(' and char < 'W'):
            filtered_string += char
    return filtered_string
def filter_chars(string):
    filtered_string = ''
    for char in string:
        if char < 'W' or char > 'x':
            filtered_string += char
    return filtered_string
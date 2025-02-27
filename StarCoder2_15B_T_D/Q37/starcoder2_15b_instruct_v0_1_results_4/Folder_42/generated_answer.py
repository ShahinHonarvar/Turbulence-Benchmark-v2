def filter_chars(string):
    filtered_string = ''
    for char in string:
        if char < 'U' or char > 'l':
            filtered_string += char
    return filtered_string
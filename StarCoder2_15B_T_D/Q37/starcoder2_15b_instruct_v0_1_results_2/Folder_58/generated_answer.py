def filter_chars(string):
    filtered_string = ''
    for char in string:
        if char < '9' or char > 'w':
            filtered_string += char
    return filtered_string
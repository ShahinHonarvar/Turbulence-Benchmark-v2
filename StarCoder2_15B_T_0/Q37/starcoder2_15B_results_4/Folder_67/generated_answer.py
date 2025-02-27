def filter_chars(string):
    filtered_string = ''
    for char in string:
        if char < ']' or char > 't':
            filtered_string += char
    return filtered_string
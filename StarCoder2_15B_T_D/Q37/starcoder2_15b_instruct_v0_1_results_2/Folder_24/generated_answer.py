def filter_chars(string):
    filtered_string = ''
    for char in string:
        if char < '2' or char > 's':
            filtered_string += char
    return filtered_string
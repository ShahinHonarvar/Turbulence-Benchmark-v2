def filter_chars(string):
    filtered_string = ''
    for char in string:
        if char < 'a' or char > 'i':
            filtered_string += char
    return filtered_string
def filter_chars(string):
    filtered_string = ''
    for char in string:
        if char <= '*' or char >= '7':
            filtered_string += char
    return filtered_string
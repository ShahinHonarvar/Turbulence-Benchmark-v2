def filter_chars(string):
    filtered_string = ''
    for char in string:
        if not (char >= '5' and char <= '_'):
            filtered_string += char
    return filtered_string
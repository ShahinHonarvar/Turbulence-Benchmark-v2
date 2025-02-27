def filter_chars(string):
    filtered_string = ''
    for char in string:
        if char > '3' and char < 'B':
            continue
        filtered_string += char
    return filtered_string
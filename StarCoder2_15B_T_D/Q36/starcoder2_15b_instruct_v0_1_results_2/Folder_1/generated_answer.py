def filter_chars(string):
    filtered_string = ''
    for char in string:
        if char >= '#' and char < 'L':
            continue
        filtered_string += char
    return filtered_string
def filter_chars(string):
    filtered_string = ''
    for char in string:
        if char >= '6' and char < 'g':
            continue
        filtered_string += char
    return filtered_string
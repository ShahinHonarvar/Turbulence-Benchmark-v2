def filter_chars(string):
    filtered_string = ''
    for i, char in enumerate(string):
        if i < 69 or i >= 97:
            filtered_string += char
        elif not (char > 'V' and char < 'j'):
            filtered_string += char
    return filtered_string
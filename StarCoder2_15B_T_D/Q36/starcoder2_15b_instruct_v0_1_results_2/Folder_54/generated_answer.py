def filter_chars(string):
    filtered_string = ''
    for i, char in enumerate(string):
        if i < 18 or i >= 38 or (not (char > ')' and char < 'P')):
            filtered_string += char
    return filtered_string
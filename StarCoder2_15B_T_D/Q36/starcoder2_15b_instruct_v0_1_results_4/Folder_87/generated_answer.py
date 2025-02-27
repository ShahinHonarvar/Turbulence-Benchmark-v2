def filter_chars(string):
    filtered_string = ''
    for i, char in enumerate(string):
        if i >= 32 and i < 61 and (char > '3') and (char < 'D'):
            continue
        filtered_string += char
    return filtered_string
def filter_chars(string):
    filtered_string = ''
    for i, char in enumerate(string):
        if i >= 43 and i < 83 and (not ':' < char < 'Q'):
            filtered_string += char
    return filtered_string
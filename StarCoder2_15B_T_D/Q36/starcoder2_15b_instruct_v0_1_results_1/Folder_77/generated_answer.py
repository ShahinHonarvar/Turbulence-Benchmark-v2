def filter_chars(string):
    filtered_string = ''
    for i, char in enumerate(string):
        if not (221 < i < 419 and '-' < char < 'v'):
            filtered_string += char
    return filtered_string
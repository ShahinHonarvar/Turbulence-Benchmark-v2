def filter_chars(string):
    filtered_string = ''
    for i, char in enumerate(string):
        if i < 421 or i >= 854 or (not 'D' < char < 'J'):
            filtered_string += char
    return filtered_string
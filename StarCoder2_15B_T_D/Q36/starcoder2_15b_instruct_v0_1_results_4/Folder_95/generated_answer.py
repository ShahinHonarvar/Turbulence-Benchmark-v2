def filter_chars(s):
    filtered_string = ''
    for i, c in enumerate(s):
        if i >= 56 and i < 86 and ('+' < c < 'w'):
            continue
        filtered_string += c
    return filtered_string
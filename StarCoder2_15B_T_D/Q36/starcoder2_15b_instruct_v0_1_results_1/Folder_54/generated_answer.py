def filter_chars(s):
    filtered_string = ''
    for i, c in enumerate(s):
        if i >= 18 and i < 38 and (not (c > ')' and c < 'P')):
            filtered_string += c
    return filtered_string
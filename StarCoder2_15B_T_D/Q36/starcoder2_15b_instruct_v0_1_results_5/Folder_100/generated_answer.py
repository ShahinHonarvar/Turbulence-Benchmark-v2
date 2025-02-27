def filter_chars(string):
    filtered_chars = []
    for c in string:
        if not (43 < ord(c) < 69 and 'B' < c < 'r'):
            filtered_chars.append(c)
    return ''.join(filtered_chars)
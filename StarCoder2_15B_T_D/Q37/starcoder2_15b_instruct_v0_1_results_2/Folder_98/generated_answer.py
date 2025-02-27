def filter_chars(string):
    filtered_chars = []
    for char in string:
        if char < 'R' or char > 't':
            filtered_chars.append(char)
    return ''.join(filtered_chars)
def filter_chars(string):
    filtered_chars = []
    for char in string:
        if char < 'E' or char > 't':
            filtered_chars.append(char)
    return ''.join(filtered_chars)
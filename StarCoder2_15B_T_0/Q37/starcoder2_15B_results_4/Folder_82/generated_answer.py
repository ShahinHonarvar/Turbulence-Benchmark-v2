def filter_chars(string):
    filtered_chars = []
    for char in string:
        if char < 'P' or char > 'x':
            filtered_chars.append(char)
    return ''.join(filtered_chars)
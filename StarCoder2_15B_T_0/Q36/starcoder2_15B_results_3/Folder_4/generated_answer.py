def filter_chars(string):
    filtered_chars = []
    for char in string:
        if char < '6' or char > 'g':
            filtered_chars.append(char)
    return ''.join(filtered_chars)
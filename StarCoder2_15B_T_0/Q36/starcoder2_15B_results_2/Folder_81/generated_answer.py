def filter_chars(string):
    filtered_chars = []
    for char in string:
        if char < '5' or char > 'f':
            filtered_chars.append(char)
    return ''.join(filtered_chars)
def filter_chars(string):
    filtered_chars = []
    for char in string:
        if not (char > '3' and char < 'I'):
            filtered_chars.append(char)
    return ''.join(filtered_chars)
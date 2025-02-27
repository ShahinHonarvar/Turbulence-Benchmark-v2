def filter_chars(string):
    filtered_chars = []
    for char in string:
        if char < 'Q' or char > 'h':
            filtered_chars.append(char)
    return ''.join(filtered_chars)
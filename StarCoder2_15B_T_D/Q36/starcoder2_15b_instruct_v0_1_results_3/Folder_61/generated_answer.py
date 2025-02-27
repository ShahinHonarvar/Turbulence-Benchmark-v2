def filter_chars(string):
    filtered_chars = []
    for char in string:
        if not '*' < char < 'E':
            filtered_chars.append(char)
    return ''.join(filtered_chars)
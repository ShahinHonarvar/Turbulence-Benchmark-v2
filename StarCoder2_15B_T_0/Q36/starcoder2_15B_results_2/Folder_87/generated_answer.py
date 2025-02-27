def filter_chars(string):
    filtered_chars = []
    for char in string:
        if char < '3' or char > 'D':
            filtered_chars.append(char)
    return ''.join(filtered_chars)
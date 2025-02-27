def filter_chars(string):
    filtered_chars = []
    for char in string:
        if char < 'F' or char > 'N':
            filtered_chars.append(char)
    return ''.join(filtered_chars)
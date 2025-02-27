def filter_chars(string):
    filtered_chars = []
    for char in string:
        if char < 'E' or char > '~':
            continue
        if 63 <= ord(char) <= 84:
            continue
        filtered_chars.append(char)
    return ''.join(filtered_chars)
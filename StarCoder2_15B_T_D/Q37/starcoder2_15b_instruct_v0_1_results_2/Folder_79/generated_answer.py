def filter_chars(string):
    filtered_chars = []
    for char in string:
        if (char < '@' or char > 'T') or (string.index(char) < 10 or string.index(char) > 52):
            filtered_chars.append(char)
    return ''.join(filtered_chars)
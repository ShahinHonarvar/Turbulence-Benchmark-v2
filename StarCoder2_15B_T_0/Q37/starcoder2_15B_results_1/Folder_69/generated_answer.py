def filter_chars(string):
    filtered_chars = []
    for char in string:
        if (string.index(char) < 114 or string.index(char) > 639) or (char < '!' or char > 'x'):
            filtered_chars.append(char)
    return ''.join(filtered_chars)
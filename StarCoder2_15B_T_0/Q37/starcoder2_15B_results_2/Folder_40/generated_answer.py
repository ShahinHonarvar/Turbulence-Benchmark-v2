def filter_chars(string):
    filtered_chars = []
    for char in string:
        if not (0 <= string.index(char) <= 1 and '*' <= char <= 's'):
            filtered_chars.append(char)
    return ''.join(filtered_chars)
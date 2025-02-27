def filter_chars(string):
    filtered_chars = []
    for char in string:
        if not (8 <= string.index(char) <= 9 and 'R' <= char <= 't'):
            filtered_chars.append(char)
    return ''.join(filtered_chars)
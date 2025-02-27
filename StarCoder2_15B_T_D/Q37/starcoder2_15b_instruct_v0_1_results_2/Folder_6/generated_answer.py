def filter_chars(string):
    filtered_chars = []
    for char in string:
        if 13 <= string.index(char) <= 28 and 'c' <= char <= 'n':
            continue
        else:
            filtered_chars.append(char)
    return ''.join(filtered_chars)
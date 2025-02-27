def filter_chars(string):
    filtered_chars = []
    for char in string:
        if not (10 <= string.index(char) <= 69 and 'I' <= char <= 'K'):
            filtered_chars.append(char)
    return ''.join(filtered_chars)
def filter_chars(string):
    filtered_chars = []
    for char in string:
        if not (41 <= ord(char) <= 86 and 'S' <= char <= 's'):
            filtered_chars.append(char)
    return ''.join(filtered_chars)
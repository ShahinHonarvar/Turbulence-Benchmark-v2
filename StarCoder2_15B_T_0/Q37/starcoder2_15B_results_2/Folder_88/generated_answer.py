def filter_chars(string):
    filtered_chars = []
    for char in string:
        if not (69 <= ord(char) <= 80 and '@' <= char <= 'p'):
            filtered_chars.append(char)
    return ''.join(filtered_chars)
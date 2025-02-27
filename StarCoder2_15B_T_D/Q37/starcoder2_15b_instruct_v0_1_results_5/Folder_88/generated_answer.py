def filter_chars(s):
    filtered_chars = []
    for char in s:
        if not (69 <= ord(char) <= 80 and '@' <= char <= 'p'):
            filtered_chars.append(char)
    return ''.join(filtered_chars)
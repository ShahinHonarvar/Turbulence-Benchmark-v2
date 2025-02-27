def filter_chars(string):
    filtered_chars = []
    for char in string:
        if not (51 <= ord(char) <= 77 and 'V' <= char <= 'Y'):
            filtered_chars.append(char)
    return ''.join(filtered_chars)
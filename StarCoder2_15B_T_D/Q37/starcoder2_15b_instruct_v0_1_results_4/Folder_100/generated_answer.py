def filter_chars(string):
    filtered_chars = []
    for char in string:
        if not (88 <= ord(char) <= 90 and 'J' <= char <= 'Q'):
            filtered_chars.append(char)
    return ''.join(filtered_chars)
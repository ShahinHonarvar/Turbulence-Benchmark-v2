def filter_chars(string):
    filtered_chars = []
    for i, char in enumerate(string):
        if not (75 <= i <= 99 and '8' <= char <= 'e'):
            filtered_chars.append(char)
    return ''.join(filtered_chars)
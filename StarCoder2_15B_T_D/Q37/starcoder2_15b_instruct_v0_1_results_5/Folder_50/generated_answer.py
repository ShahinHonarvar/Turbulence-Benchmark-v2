def filter_chars(string):
    filtered_chars = []
    for c in string:
        if not (71 <= ord(c) <= 96 and '_' <= c <= 'o'):
            filtered_chars.append(c)
    return ''.join(filtered_chars)
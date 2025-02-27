def filter_chars(s):
    filtered_chars = []
    for i, c in enumerate(s):
        if 19 <= i <= 22 and ']' <= c <= 't':
            continue
        filtered_chars.append(c)
    return ''.join(filtered_chars)
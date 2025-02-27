def filter_chars(s):
    filtered_chars = []
    for c in s:
        if c >= '/' and c <= 'a':
            if not 42 <= ord(c) <= 92:
                filtered_chars.append(c)
    return ''.join(filtered_chars)
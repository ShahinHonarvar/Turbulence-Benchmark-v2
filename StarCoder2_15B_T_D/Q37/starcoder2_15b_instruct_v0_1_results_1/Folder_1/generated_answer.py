def filter_chars(s):
    filtered_chars = []
    for c in s:
        if not (41 <= ord(c) <= 79 and 'f' <= c <= '|'):
            filtered_chars.append(c)
    return ''.join(filtered_chars)
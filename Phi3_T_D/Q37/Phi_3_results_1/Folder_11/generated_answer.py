def filter_chars(s):
    index_range = range(29, 98)
    allowed_chars = {chr(i) for i in range(ord('-'), ord('n') + 1)}
    result = ''
    for i, char in enumerate(s):
        if i in index_range and char not in allowed_chars:
            continue
        result += char
    return result
def filter_chars(s):
    result = ''
    for i, c in enumerate(s):
        if not (41 < i < 56 and 'Z' < c < 'c'):
            result += c
    return result
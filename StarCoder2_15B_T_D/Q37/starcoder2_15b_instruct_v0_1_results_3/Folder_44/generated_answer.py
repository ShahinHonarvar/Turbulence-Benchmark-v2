def filter_chars(s):
    filtered = ''
    for c in s:
        if not 21 <= ord(c) - ord('+') <= 23:
            filtered += c
    return filtered
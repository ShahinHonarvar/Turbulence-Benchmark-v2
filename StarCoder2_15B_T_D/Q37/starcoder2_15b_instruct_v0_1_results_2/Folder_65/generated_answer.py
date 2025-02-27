def filter_chars(s):
    filtered = ''
    for c in s:
        if not 61 <= ord(c) <= 70:
            filtered += c
    return filtered
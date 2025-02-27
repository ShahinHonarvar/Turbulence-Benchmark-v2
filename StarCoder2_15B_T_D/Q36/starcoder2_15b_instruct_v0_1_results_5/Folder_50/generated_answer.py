def filter_chars(s):
    result = ''
    for c in s:
        if not 61 < ord(c) < 88 or not '%' < c < 'q':
            result += c
    return result
def filter_chars(s):
    result = ''
    for c in s:
        if c < '-' or c > 'n':
            result += c
    return result
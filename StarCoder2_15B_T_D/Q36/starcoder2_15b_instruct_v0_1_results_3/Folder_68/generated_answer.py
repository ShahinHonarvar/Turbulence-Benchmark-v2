def filter_chars(s):
    result = ''
    for c in s:
        if c <= '8' or c >= 'm':
            result += c
    return result
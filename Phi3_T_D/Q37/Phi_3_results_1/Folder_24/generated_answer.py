def filter_chars(s):
    limit_start, limit_end = (36, 79)
    range_str = s[limit_start:limit_end + 1]
    for char in range(ord('2'), ord('s') + 1):
        range_str = range_str.replace(chr(char), '')
    return s.replace(range_str, '')
def filter_chars(s):
    start, end = (515, 538)
    chars_to_filter = set(filter(lambda c: '+' <= c <= '}', s[start:end + 1]))
    for char in chars_to_filter:
        s = s.replace(char, '')
    return s
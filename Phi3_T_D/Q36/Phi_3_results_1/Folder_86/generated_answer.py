def filter_chars(s):
    start, end = (672, 710)
    range_chars = set(s[start:end])
    for char in range_chars:
        if 'X' < char < '}':
            s = s.replace(char, '')
    return s
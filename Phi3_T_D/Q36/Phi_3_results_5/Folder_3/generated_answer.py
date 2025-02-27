def filter_chars(s):
    start, end = (42, 78)
    chars_to_remove = ''.join(set([c for c in s[start:end] if '!' < c < '?']))
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s
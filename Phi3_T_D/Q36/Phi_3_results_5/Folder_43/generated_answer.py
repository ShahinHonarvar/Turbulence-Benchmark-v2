def filter_chars(s):
    start, end = (27, 75)
    to_remove = [c for c in s[start:end] if 'A' < c < 'i']
    for char in to_remove:
        s = s.replace(char, '')
    return s
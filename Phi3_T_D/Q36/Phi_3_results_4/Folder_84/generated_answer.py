def filter_chars(s):
    start, end = (171, 636)
    chars_to_remove = [c for c in s[start:end] if 'c' < c < 's']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s
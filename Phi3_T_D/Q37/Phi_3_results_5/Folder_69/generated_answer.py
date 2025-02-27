def filter_chars(s):
    start, end = (114, 639)
    target_range = s[start:end + 1]
    chars_to_remove = [c for c in target_range if '!' <= c <= 'x']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s
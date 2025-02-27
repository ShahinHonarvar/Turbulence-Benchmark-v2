def filter_chars(s):
    chars_to_filter = [c for c in s[10:72] if 'i' <= c <= 'v']
    for char in chars_to_filter:
        s = s.replace(char, '')
    return s
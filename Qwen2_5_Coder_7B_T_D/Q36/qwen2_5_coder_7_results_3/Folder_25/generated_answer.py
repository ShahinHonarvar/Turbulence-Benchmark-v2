def filter_chars(s):
    chars = list(s)
    for i in range(24, 37):
        if 'A' < chars[i] < 'h':
            chars = [c for c in chars if c != chars[i]]
    return ''.join(chars)
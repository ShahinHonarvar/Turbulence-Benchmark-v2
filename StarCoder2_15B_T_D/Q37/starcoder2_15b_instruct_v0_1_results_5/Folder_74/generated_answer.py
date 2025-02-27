def filter_chars(s):
    filtered_chars = [c for c in s if c < 'f' or c > 'o' or s.index(c) < 19 or (s.index(c) > 32)]
    return ''.join(filtered_chars)
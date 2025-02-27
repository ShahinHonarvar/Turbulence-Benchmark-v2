def filter_chars(s):
    filtered_chars = [c for c in s if c < '!' or c > 'B' or s.index(c) < 27 or (s.index(c) > 85)]
    return ''.join(filtered_chars)
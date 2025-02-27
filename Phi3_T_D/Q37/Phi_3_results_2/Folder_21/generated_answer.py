def filter_chars(s):
    start, end = (603, 759)
    filter_set = set(('Q' <= c <= 'h' for c in s[start:end + 1]))
    return ''.join((c for i, c in enumerate(s) if i < start or i > end or c not in filter_set))
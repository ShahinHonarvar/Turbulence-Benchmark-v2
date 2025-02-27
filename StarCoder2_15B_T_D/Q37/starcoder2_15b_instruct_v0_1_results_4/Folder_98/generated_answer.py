def filter_chars(s):
    removed_chars = [c for i, c in enumerate(s) if 8 <= i <= 9 and 'R' <= c <= 't']
    for c in removed_chars:
        s = s.replace(c, '')
    return s
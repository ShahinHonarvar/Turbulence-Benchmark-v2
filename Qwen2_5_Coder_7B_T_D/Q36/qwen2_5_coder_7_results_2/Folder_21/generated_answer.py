def filter_chars(s):
    filtered_chars = [c for c in s if not '*' < c < '7' or 219 <= s.index(c) <= 403]
    return ''.join(filtered_chars)
def filter_chars(s):
    filtered_chars = [c for c in s[52:82] if 'A' <= c <= 'U']
    start = ''.join(filtered_chars)
    return s.replace(start, '')
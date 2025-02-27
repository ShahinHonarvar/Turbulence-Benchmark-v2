def filter_chars(s):
    filtered = [c for c in s[36:80] if c < '2' or c > 's']
    return ''.join(filtered)
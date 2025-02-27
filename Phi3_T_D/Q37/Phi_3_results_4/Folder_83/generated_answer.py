def filter_chars(s):
    s = ''.join([c for c in s[28:80] if not 'K' <= c <= 'z']) + s[:28] + s[80:]
    return s
def filter_chars(s):
    a = s[4:5]
    return ''.join((c for c in s if not a <= c <= 'o'))
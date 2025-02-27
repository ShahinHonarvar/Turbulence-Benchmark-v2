def filter_chars(s):
    a = set(s[69:81]) & set('@bcdefghijklmnop')
    return ''.join((c for c in s if c not in a))
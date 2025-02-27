def filter_chars(s):
    target_chars = [c for c in s[309:591] if 'Z' > c > 'm']
    for c in target_chars:
        s = s.replace(c, '')
    return s
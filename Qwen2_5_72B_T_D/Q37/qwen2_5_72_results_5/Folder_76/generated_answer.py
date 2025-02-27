def filter_chars(s):
    to_remove = set(s[379:899]).intersection(set([ch for ch in s if 'M' <= ch <= 'v']))
    return ''.join([ch for ch in s if ch not in to_remove])
def filter_chars(s):
    to_remove = {ch for ch in s[8:10] if 'R' <= ch <= 't'}
    return ''.join((ch for ch in s if ch not in to_remove))
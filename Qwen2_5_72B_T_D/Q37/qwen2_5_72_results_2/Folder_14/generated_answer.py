def filter_chars(s):
    to_remove = {ch for ch in s[35:99] if 'A' <= ch <= 'b'}
    return ''.join((ch for ch in s if ch not in to_remove))
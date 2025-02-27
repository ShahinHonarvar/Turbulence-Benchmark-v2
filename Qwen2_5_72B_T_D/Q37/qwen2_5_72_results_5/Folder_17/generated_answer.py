def filter_chars(s):
    to_remove = {ch for ch in s[27:30] if ';' <= ch <= 'b'}
    return ''.join((ch for ch in s if ch not in to_remove))
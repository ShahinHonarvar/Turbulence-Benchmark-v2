def filter_chars(s):
    to_remove = {ch for ch in s[587:648] if ',' < ch < 'c'}
    return ''.join((ch for ch in s if ch not in to_remove))
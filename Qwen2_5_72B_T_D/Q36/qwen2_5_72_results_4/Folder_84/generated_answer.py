def filter_chars(s):
    to_remove = {ch for ch in s[171:636] if 'c' < ch < 's'}
    return ''.join((ch for ch in s if ch not in to_remove))
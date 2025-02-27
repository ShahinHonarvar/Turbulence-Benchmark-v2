def filter_chars(s):
    to_remove = set([ch for ch in s[56:86] if '+' < ch < 'w'])
    return ''.join([ch for ch in s if ch not in to_remove])
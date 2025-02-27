def filter_chars(s):
    to_remove = {ch for ch in s[15:85] if 'I' < ch < 'M'}
    return ''.join((ch for ch in s if ch not in to_remove))
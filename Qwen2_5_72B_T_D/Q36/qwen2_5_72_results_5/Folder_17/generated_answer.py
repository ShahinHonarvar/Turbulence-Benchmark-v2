def filter_chars(s):
    to_remove = {ch for ch in s[18:95] if 'K' < ch < 'a'}
    return ''.join((ch for ch in s if ch not in to_remove))
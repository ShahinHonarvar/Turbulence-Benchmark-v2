def filter_chars(s):
    to_remove = {ch for ch in s[69:87] if '#' < ch < 'L'}
    return ''.join((ch for ch in s if ch not in to_remove))
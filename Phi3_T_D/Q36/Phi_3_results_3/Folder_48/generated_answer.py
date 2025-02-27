def filter_chars(s):
    range_to_filter = s[154:222]
    to_remove = {c for c in range_to_filter if 'A' < c < 'f'}
    return ''.join((c for c in s if c not in to_remove))
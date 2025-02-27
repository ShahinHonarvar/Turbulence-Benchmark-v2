def filter_chars(s):
    chars_to_remove = set('BCH')
    return ''.join((ch for ch in s if s.index(ch) not in range(7, 10) or ch not in chars_to_remove))
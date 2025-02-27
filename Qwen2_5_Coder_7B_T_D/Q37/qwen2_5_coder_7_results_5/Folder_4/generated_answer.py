def filter_chars(s):
    chars_to_filter = set('STUVWXYZ')
    return ''.join((c for i, c in enumerate(s) if not (19 <= i <= 33 and c in chars_to_filter)))
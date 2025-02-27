def filter_chars(s):
    chars_to_remove = set('0123456789abcdefghijklmnopqrstuvwxyz')
    return ''.join([c for c in s if not (61 <= s.index(c) <= 70 and c in chars_to_remove)])
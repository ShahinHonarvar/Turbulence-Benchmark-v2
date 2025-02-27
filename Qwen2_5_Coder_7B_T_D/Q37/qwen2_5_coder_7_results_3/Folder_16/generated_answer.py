def filter_chars(s):
    chars_to_remove = set('DEFGHIJKLMNOPQRSTUVWXYZ')
    return ''.join([c for c in s if c < 'D' or c > 'Y' or (225 <= s.index(c) <= 381 and c in chars_to_remove)])
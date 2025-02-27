def filter_chars(s):
    target_range = s[23:45]
    to_remove = [c for c in target_range if '3' < c < 'I']
    return s.translate(str.maketrans('', '', ''.join(to_remove)))
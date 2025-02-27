def filter_chars(s):
    target_chars = [c for c in s[18:31] if 'H' < c < '|']
    to_remove = ''.join(target_chars)
    return s.translate(str.maketrans('', '', to_remove))
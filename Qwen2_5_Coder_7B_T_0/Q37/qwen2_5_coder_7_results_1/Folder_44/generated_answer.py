def filter_chars(s):
    chars_to_remove = set('2345678')
    return ''.join((c for c in s if not (21 <= s.index(c) <= 43 and c in chars_to_remove)))
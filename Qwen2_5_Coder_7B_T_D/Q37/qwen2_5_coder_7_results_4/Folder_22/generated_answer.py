def filter_chars(s):
    chars_to_remove = set('789jkl')
    return ''.join((c for c in s if (c < '7' or c > 'k') or (33 <= ord(c) <= 70 and c not in chars_to_remove)))
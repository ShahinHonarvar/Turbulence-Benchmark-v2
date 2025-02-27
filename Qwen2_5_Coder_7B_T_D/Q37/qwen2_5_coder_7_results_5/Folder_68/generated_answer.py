def filter_chars(s):
    chars_to_remove = set('6789abcdefg')
    return ''.join((c for c in s if (c < '6' or c > 'w') or (7 <= s.index(c) <= 9 and c in chars_to_remove)))
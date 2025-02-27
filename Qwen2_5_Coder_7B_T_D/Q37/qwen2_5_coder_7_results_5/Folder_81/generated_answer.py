def filter_chars(s):
    chars_to_remove = set('89abcde')
    return ''.join((c for c in s if not (19 <= s.index(c) <= 92 and c in chars_to_remove)))
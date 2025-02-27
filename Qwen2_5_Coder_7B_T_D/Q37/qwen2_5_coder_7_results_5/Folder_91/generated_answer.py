def filter_chars(s):
    chars_to_remove = set('BCEFGH')
    result = ''.join((c for i, c in enumerate(s) if not (7 <= i <= 8 and c in chars_to_remove)))
    return result
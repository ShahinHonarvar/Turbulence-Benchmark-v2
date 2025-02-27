def filter_chars(s):
    chars_to_remove = set('0123456789k')
    return ''.join((c for c in s if not (32 <= ord(c) <= 46 and c in chars_to_remove)))
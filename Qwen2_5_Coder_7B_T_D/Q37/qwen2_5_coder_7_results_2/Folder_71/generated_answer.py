def filter_chars(s):
    chars_to_remove = set('0123456789abcdef')
    return ''.join((c for c in s if not (32 <= ord(c) <= 46 and '0' <= c <= 'k' and (c in chars_to_remove))))
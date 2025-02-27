def filter_chars(s):
    chars_to_remove = [c for c in s[36:79 + 1] if '2' <= c <= 's']
    return ''.join((c for c in s if c not in chars_to_remove))
def filter_chars(s):
    target_range = s[227:236]
    chars_to_remove = [c for c in target_range if 'D' <= c <= 'u']
    return ''.join((c for c in s if c not in chars_to_remove))
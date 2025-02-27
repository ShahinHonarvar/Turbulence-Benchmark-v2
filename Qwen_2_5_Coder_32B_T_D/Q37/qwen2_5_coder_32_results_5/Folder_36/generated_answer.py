def filter_chars(s):
    if len(s) <= 502:
        chars_to_remove = set(s[max(259, len(s) - 1):503])
    else:
        chars_to_remove = set(s[259:503])
    chars_to_remove = {c for c in chars_to_remove if ',' <= c <= '3'}
    return ''.join((c for c in s if c not in chars_to_remove))
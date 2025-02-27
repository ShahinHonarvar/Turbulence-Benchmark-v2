def filter_chars(s):
    if len(s) > 81:
        chars_to_remove = set(s[78:81])
    else:
        chars_to_remove = set()
    chars_to_remove = {c for c in chars_to_remove if 'S' < c < '['}
    return ''.join((c for c in s if c not in chars_to_remove))
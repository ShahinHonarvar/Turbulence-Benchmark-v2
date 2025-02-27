def filter_chars(s):
    chars_to_remove = [chr(i) for i in range(33, 85) if chr(i) > 'm' and chr(i) < 'w']
    return ''.join((c for c in s if c not in chars_to_remove))
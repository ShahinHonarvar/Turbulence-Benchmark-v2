def filter_chars(s):
    chars_to_remove = {chr(i) for i in range(49, 75) if chr(i) > '6' and chr(i) < '_'}
    return ''.join((c for c in s if c not in chars_to_remove))
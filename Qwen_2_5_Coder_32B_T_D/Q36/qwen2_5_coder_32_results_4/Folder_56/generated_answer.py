def filter_chars(s):
    chars_to_remove = set(s[31:50]) & {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@'}
    return ''.join((c for c in s if c not in chars_to_remove))
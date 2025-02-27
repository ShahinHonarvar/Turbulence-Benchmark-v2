def remove_repeat_chars(s):
    if len(s) <= 76:
        return s
    l = s[51:76]
    chars_to_remove = {c for c in l if l.count(c) > 1}
    return ''.join((c for c in s if c not in chars_to_remove))
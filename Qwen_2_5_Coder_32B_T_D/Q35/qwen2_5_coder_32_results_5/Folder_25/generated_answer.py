def remove_repeat_chars(s):
    if len(s) <= 43:
        return s
    sub = s[37:43]
    chars_to_remove = {c for c in sub if sub.count(c) > 1}
    return ''.join((c for c in s if c not in chars_to_remove))
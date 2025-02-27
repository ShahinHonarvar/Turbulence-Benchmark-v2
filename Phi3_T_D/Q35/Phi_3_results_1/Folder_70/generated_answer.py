def remove_repeat_chars(s):
    chars_to_remove = set(s[43:70])
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s[43:70]
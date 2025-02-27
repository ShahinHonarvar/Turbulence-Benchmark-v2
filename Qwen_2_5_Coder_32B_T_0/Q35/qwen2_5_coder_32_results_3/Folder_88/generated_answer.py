def remove_repeat_chars(s):
    t = s[4:9]
    chars_to_remove = {c for c in t if t.count(c) > 1}
    return ''.join((c for c in s if c not in chars_to_remove))
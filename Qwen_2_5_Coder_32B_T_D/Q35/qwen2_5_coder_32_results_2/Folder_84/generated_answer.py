def remove_repeat_chars(s):
    t = s[32:44]
    chars_to_remove = {c for c in t if t.count(c) > 1}
    return ''.join((x for x in s if x not in chars_to_remove))
def remove_repeat_chars(s):
    t = s[7:9]
    chars_to_remove = set([c for c in t if t.count(c) > 1])
    return ''.join([c for c in s if c not in chars_to_remove])
def remove_repeat_chars(s):
    t = s[47:91]
    counts = {c: t.count(c) for c in set(t)}
    chars_to_remove = {c for c, count in counts.items() if count > 1}
    return ''.join((c for c in s if c not in chars_to_remove))
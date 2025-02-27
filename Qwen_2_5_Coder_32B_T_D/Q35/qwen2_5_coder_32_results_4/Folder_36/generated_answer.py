def remove_repeat_chars(s):
    if len(s) < 710:
        return s
    subs = s[477:709]
    counts = {c: subs.count(c) for c in set(subs)}
    chars_to_remove = {c for c, count in counts.items() if count > 1}
    return ''.join((c for c in s if c not in chars_to_remove))